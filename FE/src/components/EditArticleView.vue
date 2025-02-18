<template>
    <v-container>
      <v-card v-if="article">
        <v-card-title>Edit Article</v-card-title>
        <v-card-text>
          <ArticleForm :existingArticle="article" @article-saved="goToHome" />
        </v-card-text>
      </v-card>
    </v-container>
  </template>
  
  <script>
  import { ref, onMounted } from 'vue';
  import { useRoute, useRouter } from 'vue-router';
  import { getArticleById } from '@/api';
  import ArticleForm from '@/components/ArticleForm.vue';
  
  export default {
    components: { ArticleForm },
    setup() {
      const route = useRoute();
      const router = useRouter();
      const article = ref(null);
  
      onMounted(async () => {
        article.value = await getArticleById(route.params.id);
      });
  
      const goToHome = () => {
        router.push('/');
      };
  
      return { article, goToHome };
    }
  };
  </script>
  