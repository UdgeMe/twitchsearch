<template>
  <div class="game-search">
    <input
      v-model="query"
      @input="fetchGames"
      type="text"
      placeholder="Rechercher un jeu..."
    />
    <ul v-if="games.length > 0">
      <li v-for="game in games" :key="game.id" @click="selectGame(game)">
        {{ game.name }}
      </li>
    </ul>
    <p v-if="error">{{ error }}</p>
  </div>
</template>

<script>
import { ref } from "vue";

export default {
  setup(_, { emit }) {
    // valeur de la recherche
    const query = ref("");
    // "liste" des jeux trouvés (Twitch ne fait que de la recherche exacte donc on ne verra qu'un seul jeu a priori...)
    const games = ref([]);
    // erreur éventuelle lors de l'ajout d'un nouveau jeu
    const error = ref(null);

    // méthode de fetch des jeux en fonction de la recherche
    const fetchGames = async () => {
      if (query.value.length < 2) {
        games.value = [];
        return;
      }
      error.value = null;

      const response = await fetch(
        `http://localhost:8000/search-game/${query.value}`
      );
      const data = await response.json();
      games.value = data || [];
    };

    // méthode lors du choix d'un jeu dans la "liste" proposée
    const selectGame = async (game) => {
      query.value = game.name;
      games.value = [];

      // appel de l'api pour ajouter le jeu
      await saveGameQuery(game);
    };

    // méthode d'ajout de jeu dans la base
    const saveGameQuery = async (game) => {
      try {
        const response = await fetch(
          'http://localhost:8000/save-game-query/',
          {
            method: "POST",
            headers: {
              "Content-Type": "application/json",
            },
            body: JSON.stringify(game),
          },
        );
        if (!response.ok) throw new Error("Erreur lors de l'ajout d'un nouveau jeu");
        const data = await response.json();
        if (data === 'game saved') {
          emit("gameAdded");
        } else if (data === 'game already in db') {
          throw new Error("Le jeu est déjà dans votre liste")
        }
      } catch (err) {
        error.value = err.message;
      }
    };
    return { query, error, games, fetchGames, selectGame };
  },
};
</script>

<style scoped>
.game-search {
  position: relative;
  width: 300px;
}
input {
  width: 300px;
  padding: 8px;
}
ul {
  position: absolute;
  width: 100%;
  background: white;
  border: 1px solid #cccccc;
  list-style: none;
  padding: 0;
  margin: 0;
}
li {
  padding: 8px;
  cursor: pointer;
  color: #000000;
}
li:hover {
  background: #f0f0f0;
}
</style>
