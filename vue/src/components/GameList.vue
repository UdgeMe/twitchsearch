<template>
  <div class="game-list">
    <h2>Liste des Jeux</h2>

    <ul v-if="games.length > 0">
      <li v-for="game in games" :key="game.id" @click="selectOneOfMyGames(game.id)" :class="{ selected: game.id === selectedGameId }">
        <img :src="game.img" :alt="game.name" class="game-image" />
        <span>{{ game.name }}</span>
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

    // méthode exécutée lors du choix d'un jeu dans la liste des jeux surveillés
    const selectOneOfMyGames = (gameId) => {
      emit("gameSelected", gameId);
    };

    // méthode de refresh de la liste des jeux
    const refreshGames = () => {
      fetchGames();
    };

    onMounted(fetchGames);

    return { games, selectOneOfMyGames, refreshGames };
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
  cursor: pointer;
}

li:hover:not(.selected) {
  background-color: #333333;
}
li.selected {
  background-color: #555555;
}

.game-image {
  width: 100px;
  height: 130px;
  object-fit: cover;
  border-radius: 5px;
}
</style>
