<template>
  <v-container>
    <v-card v-if="article">
      <v-card-title>{{ article.title }}</v-card-title>
      <v-card-subtitle>{{ article.category }}</v-card-subtitle>
      <v-card-text>
        <p>{{ article.content }}</p>
      </v-card-text>
      <v-card-actions>
        <v-btn @click="$router.push('/article/preview')">Back</v-btn>
      </v-card-actions>
    </v-card>
    <v-alert v-else type="error">Article not found</v-alert>
  </v-container>
</template>

<script>
import { getArticleById } from '@/api';

export default {
  data() {
    return {
      article: null
    };
  },
  async created() {
    const id = this.$route.params.id;
    this.article = await getArticleById(id);
  }
};
</script>