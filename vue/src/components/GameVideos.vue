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
import { onUnmounted, ref, watch } from "vue";

export default {
  props: {
    selectedGameId: String,
  },
  setup(props) {
    // liste des vidéos
    const videos = ref([]);
    const loading = ref(false);
    const error = ref(null);
    // On va utiliser un WebSocket pour que le back mette à jour régulièrement
    // les résultats
    let socket = null;

    const connectWebSocket = () => {
      if (socket) {
        // Si jamais il y avait déjà un WebSocket on le ferme
        socket.close();
      }

      // On réinitialise les valeurs du composant et on instancie le websocket avec le bon ID de jeu
      loading.value = true;
      error.value = null;
      socket = new WebSocket(`ws://localhost:8000/ws/get-videos/${props.selectedGameId}`);

      socket.onerror = () => {
        error.value = 'Une erreur est survenue';
      };
      socket.onmessage = (event) => {
        // Récupération de la liste des vidéos
        videos.value = JSON.parse(event.data);
        loading.value = false;
      };
    };

    // Lorsque l'id de jeu sélectionné change, on relance un WebSocket
    watch(() => props.selectedGameId, (gameId, prevGameId) => {
      if (gameId && prevGameId !== gameId) {
        connectWebSocket();
      }
    });

    onUnmounted(() => {
      if (socket) {
        socket.close();
      }
    });

    return { videos, loading, error };
  },
};
</script>

<style scoped>
.game-videos ul { list-style: none; padding: 0; display: flex; flex-wrap: wrap; gap: 10px; }
.game-videos li { width: 200px; }
.video-thumbnail { width: 100%; border-radius: 5px; }
</style>
