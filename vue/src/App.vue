<template>
  <div class="app-content">
    <div>
      <h1>Tapez le nom complet d'un jeu vidéo puis sélectionnez le dans les propositions pour l'ajouter à votre liste</h1>
      <GameSearch @gameAdded="refreshGames"/>
    </div>
    <div class="results">
      <GameList
        ref="gameListRef"
        @gameSelected="handleGameSelection"
        :selectedGameId="selectedGameId"
      />
      <GameVideos :selectedGameId="selectedGameId" />
    </div>
  </div>
</template>

<script>
import { ref } from "vue";
import GameList from "./components/GameList.vue";
import GameSearch from "./components/GameSearch.vue";
import GameVideos from "./components/GameVideos.vue";

export default {
  components: { GameSearch, GameList, GameVideos },
  setup() {
    // Id du jeu sélectionné dans la partie "results" en bas de page
    const selectedGameId = ref(null);
    // ref pour refresh la liste des jeux quand on en ajoute un (Cf. méthode refreshGames plus bas)
    const gameListRef = ref(null);

    // changement de l'id de jeu sélectionné
    const handleGameSelection = (gameId) => {
      selectedGameId.value = gameId;
    };

    const refreshGames = () => {
      if (gameListRef.value) {
        gameListRef.value.fetchGames();
      }
    };

    return { selectedGameId, handleGameSelection, refreshGames, gameListRef };
  },
};
</script>
<style>
.app-content {
  display: flex;
  flex-direction: column;
}
.results {
  margin-top: 80px;
  display: flex;
  flex-direction: row;
}
</style>