<template>
  <v-container class="fill-height d-flex justify-center align-center">
    <v-card width="600" class="pa-4">
      <v-card-title>
        <v-btn icon @click="goToHome">
          <v-icon>mdi-arrow-left</v-icon>
        </v-btn>
        Add New Article
      </v-card-title>
    </v-card>
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

<style scoped>
.fill-height {
  height: 100vh;
}
</style>