<template>
  <div>
    <h1>Tapez le nom complet d'un jeu vidéo</h1>
    <GameSearch />
  </div>
</template>

<script>
import GameSearch from "./components/GameSearch.vue";

export default {
  components: { GameSearch },
};
</script>
