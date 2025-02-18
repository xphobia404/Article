<template>
  <v-container>
    <v-btn class="mb-4" icon @click="$router.push('/')">
      <v-icon>mdi-arrow-left</v-icon>
    </v-btn>

    <v-card class="mb-4">
      <v-card-title>Published Articles</v-card-title>
    </v-card>

    <v-row>
      <v-col v-for="article in paginatedArticles" :key="article.id" cols="12" md="6" lg="4">
        <v-card>
          <v-card-title>{{ article.title }}</v-card-title>
          <v-card-subtitle>{{ article.category }}</v-card-subtitle>
          <v-card-text>
            {{ article.content.substring(0, 100) }}...
          </v-card-text>
          <v-card-actions>
            <v-btn color="primary" :to="'/article/' + article.id">Read More</v-btn>
          </v-card-actions>
        </v-card>
      </v-col>
    </v-row>

    <v-pagination v-model="page" :length="totalPages" rounded class="mt-4"></v-pagination>
  </v-container>
</template>

<script>
import { ref, computed, onMounted } from 'vue';
import { getArticles } from '@/api';

export default {
  setup() {
    const articles = ref([]);
    const page = ref(1);
    const itemsPerPage = 6;

    const fetchArticles = async () => {
      const allArticles = await getArticles();
      articles.value = allArticles.filter(article => article.status === 'publish');
    };

    onMounted(fetchArticles);

    const totalPages = computed(() => Math.ceil(articles.value.length / itemsPerPage));

    const paginatedArticles = computed(() => {
      const start = (page.value - 1) * itemsPerPage;
      return articles.value.slice(start, start + itemsPerPage);
    });

    return {
      articles,
      page,
      totalPages,
      paginatedArticles
    };
  }
};
</script>