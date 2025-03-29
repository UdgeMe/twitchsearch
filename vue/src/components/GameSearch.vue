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
  </div>
</template>

<script>
import { ref } from "vue";

export default {
  setup() {
    const query = ref("");
    const games = ref([]);

    const fetchGames = async () => {
      if (query.value.length < 2) {
        games.value = [];
        return;
      }

      const response = await fetch(
        `http://localhost:8000/search-game/${query.value}`
      );
      const data = await response.json();
      games.value = data || [];
    };

    const selectGame = async (game) => {
      query.value = game.name;
      games.value = [];

      await saveGameQuery(game);
    };

    const saveGameQuery = async (game) => {
        await fetch(
          'http://localhost:8000/save-game-query/',
          {
            method: "POST",
            headers: {
              "Content-Type": "application/json",
            },
            body: JSON.stringify(game),
          },
        );
    };
    return { query, games, fetchGames, selectGame };
  },
};
</script>

<style>
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
