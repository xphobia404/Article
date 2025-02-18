<template>
  <v-container>
    <v-btn color="primary" class="mb-4 mr-2" @click="$router.push('/add-article')">Add Article</v-btn>
    <v-btn color="secondary" class="mb-4" @click="$router.push('/article/preview')">preview</v-btn>

    <v-tabs v-model="selectedTab">
      <v-tab value="publish">Published</v-tab>
      <v-tab value="draft">Drafts</v-tab>
      <v-tab value="trash">Trashed</v-tab>
    </v-tabs>

    <v-data-table :headers="headers" :items="filteredArticles">
      <template #item.actions="{ item }">
        <v-icon @click="openEditDialog(item)" tabindex="0">mdi-pencil</v-icon>
        <v-icon @click="moveToTrash(item)" tabindex="0">mdi-trash-can</v-icon>
      </template>
    </v-data-table>

    <!-- Dialog untuk edit artikel -->
    <v-dialog v-model="dialog" max-width="600px">
      <v-card>
        <v-card-title>Edit Article</v-card-title>
        <v-card-text>
          <ArticleForm :existingArticle="selectedArticle" @article-saved="closeDialog" />
        </v-card-text>
      </v-card>
    </v-dialog>
  </v-container>
</template>

<script>
import { getArticles, updateArticle } from '@/api';
import ArticleForm from '@/components/ArticleForm.vue';

export default {
  components: { ArticleForm },
  data() {
    return {
      selectedTab: 'publish',
      articles: [],
      dialog: false,
      selectedArticle: null,
      headers: [
        { title: 'Title', value: 'title' },
        { title: 'Category', value: 'category' },
        { title: 'Actions', value: 'actions', sortable: false }
      ]
    };
  },
  computed: {
    filteredArticles() {
      return this.articles.filter(article => article.status === this.selectedTab);
    }
  },
  methods: {
    async fetchArticles() {
      this.articles = await getArticles();
    },
    openEditDialog(article) {
      this.selectedArticle = { ...article };
      this.dialog = true;
    },
    closeDialog() {
      this.dialog = false;
      this.fetchArticles();
    },
    async moveToTrash(article) {
      article.status = 'trash';
      await updateArticle(article);
      this.fetchArticles();
    }
  },
  created() {
    this.fetchArticles();
  }
};
</script>
