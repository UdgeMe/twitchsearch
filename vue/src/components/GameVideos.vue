<template>
  <div v-if="selectedGameId" class="game-videos">
    <h2>Vidéos du jeu</h2>
    <p v-if="loading">Chargement des vidéos...</p>
    <p v-if="error">{{ error }}</p>

    <ul v-if="!loading && videos.length > 0">
      <li v-for="video in videos" :key="video.id">
        <a :href="video.url" target="_blank">
          <img :src="video.thumbnail_url" :alt="video.title" class="video-thumbnail" />
        </a>
        <p>{{ video.title }}</p>
      </li>
    </ul>

    <p v-else-if="!loading && !error">Aucune vidéo trouvée.</p>
  </div>
</template>

<script>
import { ref, watch } from "vue";

export default {
  props: {
    selectedGameId: String,
  },
  setup(props) {
    // liste des vidéos
    const videos = ref([]);
    const loading = ref(false);
    const error = ref(null);

    // méthode de fetch des vidéos pour un id de jeu donné
    const fetchVideos = async () => {
      if (!props.selectedGameId) return;

      loading.value = true;
      error.value = null;

      try {
        const response = await fetch(`http://localhost:8000/get-videos/${props.selectedGameId}`);
        if (!response.ok) throw new Error("Erreur lors de la récupération des vidéos");

        const data = await response.json();
        videos.value = data;
      } catch (err) {
        error.value = err.message;
      } finally {
        loading.value = false;
      }
    };

    watch(() => props.selectedGameId, fetchVideos);

    return { videos, loading, error };
  },
};
</script>

<style scoped>
.game-videos ul { list-style: none; padding: 0; display: flex; flex-wrap: wrap; gap: 10px; }
.game-videos li { width: 200px; }
.video-thumbnail { width: 100%; border-radius: 5px; }
</style>
