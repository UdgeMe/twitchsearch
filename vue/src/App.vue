<template>
  <div>
    <h1>Tapez le nom complet du jeu qui vous intéresse</h1>
    <GameSearch @gameSelected="handleGameSelection" />
  </div>
</template>

<script>
import GameSearch from "./components/GameSearch.vue";
import { ref } from "vue";

export default {
  components: { GameSearch },
  setup() {
    const selectedGame = ref(null);

    const handleGameSelection = (game) => {
      selectedGame.value = game;
    };

    return { selectedGame, handleGameSelection };
  },
};
</script>
