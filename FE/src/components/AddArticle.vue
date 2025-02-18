<template>
  <v-container class="fill-height d-flex justify-center align-center">
    <v-card width="600" class="pa-4">
      <v-card-title class="d-flex align-center mb-3">
        <v-btn class="mr-2" icon @click="$router.push('/')">
          <v-icon>mdi-arrow-left</v-icon>
        </v-btn>
        <span>Add New Article</span>
      </v-card-title>

      <v-card-text>
        <v-form @submit.prevent="submitForm">
          <v-text-field v-model="article.title" label="Title" required></v-text-field>
          <v-textarea v-model="article.content" label="Content" required></v-textarea>
          <v-select v-model="article.category" :items="categories" label="Category" required></v-select>

          <v-card-actions class="d-flex justify-end">
            <v-btn color="secondary" @click="saveAsDraft">Save as Draft</v-btn>
            <v-btn color="primary" type="submit">Publish</v-btn>
          </v-card-actions>
        </v-form>
      </v-card-text>
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
      categories: [
      'Tech', 'Health', 'Lifestyle', 'Business & Finance', 'Education', 'Entertainment', 
      'Science', 'Politics & News', 'Sports', 'Food & Culinary', 'DIY & Home Improvement', 
      'Travel & Adventure', 'Automotive', 'Personal Development', 'Career & Jobs', 
      'Gaming', 'Cryptocurrency & Blockchain', 'Parenting & Family', 'Pets & Animals', 
      'Spirituality & Religion'
      ],
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
        this.$router.push('/');
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