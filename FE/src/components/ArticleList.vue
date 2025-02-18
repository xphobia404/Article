<template>
  <v-container>
    <v-tabs v-model="selectedTab">
      <v-tab value="published">Published</v-tab>
      <v-tab value="drafts">Drafts</v-tab>
      <v-tab value="trashed">Trashed</v-tab>
    </v-tabs>

    <v-data-table :headers="headers" :items="filteredArticles">
      <template #item.actions="{ item }">
        <v-icon @click="editArticle(item)">mdi-pencil</v-icon>
        <v-icon @click="moveToTrash(item)">mdi-trash-can</v-icon>
      </template>
    </v-data-table>
  </v-container>
</template>

<script>
import { getArticles, updateArticle } from '@/api';

export default {
  data() {
    return {
      selectedTab: 'published',
      articles: [],
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
    editArticle(article) {
      this.$emit('edit-article', article);
    },
    async moveToTrash(article) {
      article.status = 'trashed';
      await updateArticle(article);
      this.fetchArticles();
    }
  },
  created() {
    this.fetchArticles();
  }
};
</script>