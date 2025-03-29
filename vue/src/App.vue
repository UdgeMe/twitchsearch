<template>
  <div class="app-content">
    <div>
      <h1>Tapez le nom complet d'un jeu vidéo</h1>
      <GameSearch />
    </div>
    <div class="results">
      <GameList />
      <div>videos ici</div>
    </div>
  </div>
</template>

<script>
import GameList from "./components/GameList.vue";
import GameSearch from "./components/GameSearch.vue";

export default {
  components: { GameSearch, GameList },
};
</script>
<style>
.app-content {
  display: flex;
  flex-direction: column;
}
.results {
  display: flex;
  flex-direction: row;
}
</style>