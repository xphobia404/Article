<template>
  <v-container>
    <v-form @submit.prevent="submitForm">
      <v-text-field v-model="article.title" label="Title" required></v-text-field>
      <v-textarea v-model="article.content" label="Content" required></v-textarea>
      <v-select v-model="article.category" :items="categories" label="Category" required></v-select>
      <v-btn class="mr-2" color="primary" @click="submitForm">Publish</v-btn>
      <v-btn color="secondary" @click="saveAsDraft">Draft</v-btn>
    </v-form>
  </v-container>
</template>

<script>
import { createArticle, updateArticle } from '@/api';

export default {
  props: ['existingArticle'],
  data() {
    return {
      article: this.existingArticle || { title: '', content: '', category: '', status: 'draft' },
      categories: ['Tech', 'Health', 'Lifestyle'],
    };
  },
  methods: {
    async submitForm() {
      this.article.status = 'publish';
      await this.saveArticle();
    },
    async saveAsDraft() {
      this.article.status = 'draft';
      await this.saveArticle();
    },
    async saveArticle() {
      try {
        if (this.article.id) {
          await updateArticle(this.article);
        } else {
          await createArticle(this.article);
        }
        this.$emit('article-saved');
      } catch (error) {
        console.error('Error saving article:', error);
      }
    },
  },
};
</script>