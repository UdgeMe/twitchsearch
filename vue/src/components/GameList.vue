<template>
  <div class="game-list">
    <h2>Liste des Jeux</h2>

    <ul v-if="games.length > 0">
      <li v-for="game in games" :key="game.id" :class="{ selected: game.id === selectedGameId }">
        <div @click="selectOneOfMyGames(game.id)" class="game-title-container">
          <img :src="game.img" :alt="game.name" class="game-image" />
          <span>{{ game.name }}</span>
        </div>
        <span class="delete-game-btn" title="Supprimer le jeu de la liste" @click="deleteGame(game.id)">X</span>
      </li>
    </ul>

  </div>
</template>

<script>
import { ref, onMounted } from "vue";

export default {
  props: {
    selectedGameId: String,
  },
  setup(_, { emit }) {
    // liste des jeux
    const games = ref([]);

    // méthode de fetch de la liste des jeux "surveillés"
    const fetchGames = async () => {
      const response = await fetch('http://localhost:8000/my-games');

      games.value = await response.json();
    };

    // méthode de suppression d'un jeu dans a liste
    const deleteGame = async (gameId) => {
      await fetch(
        `http://localhost:8000/game/${gameId}`,
        { method: "DELETE" },
      );
      fetchGames();
    };


    // méthode exécutée lors du choix d'un jeu dans la liste des jeux surveillés
    const selectOneOfMyGames = (gameId) => {
      emit("gameSelected", gameId);
    };

    onMounted(fetchGames);

    return { games, selectOneOfMyGames, fetchGames, deleteGame };
  },
};
</script>

<style scoped>
.game-list {
  flex-basis: 300px;
  flex-shrink: 0;
  margin-right: 40px;
}

ul {
  list-style: none;
  padding: 0;
}

li {
  display: flex;
  align-items: center;
  gap: 10px;
  margin: 10px 0;
  position: relative;
}
.game-title-container {
  width: 270px;
    display: flex;
    align-items: center;
    cursor: pointer;
    gap: 10px;
}
.delete-game-btn {
  position: absolute;
  right: 0;
  top: 0;
  cursor: pointer;
}

li:hover:not(.selected) .game-title-container {
  background-color: #333333;
}
li.selected .game-title-container {
  background-color: #555555;
}

.game-image {
  width: 100px;
  height: 130px;
  object-fit: cover;
  border-radius: 5px;
}
</style>
