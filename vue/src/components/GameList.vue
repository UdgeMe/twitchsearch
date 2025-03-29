<template>
  <div class="game-list">
    <h2>Liste des Jeux</h2>

    <ul v-if="games.length > 0">
      <li v-for="game in games" :key="game.id" @click="getVideos(game.id)">
        <img :src="game.img" :alt="game.name" class="game-image" />
        <span>{{ game.name }}</span>
      </li>
    </ul>

  </div>
</template>

<script>
import { ref, onMounted } from "vue";

export default {
  setup() {
    const games = ref([]);

    const fetchGames = async () => {
      const response = await fetch('http://localhost:8000/my-games');

      games.value = await response.json();
    };

    onMounted(fetchGames);

    return { games };
  },
};
</script>

<style scoped>
.game-list {
  text-align: center;
  flex-basis: 200px;
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
}

.game-image {
  width: 100px;
  height: 130px;
  object-fit: cover;
  border-radius: 5px;
}
</style>
