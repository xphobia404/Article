import { createRouter, createWebHistory } from 'vue-router';
import HomeView from '@/views/HomeView.vue';
import ArticleView from '@/views/ArticleView.vue';
import ArticleForm from '@/components/ArticleForm.vue';

const routes = [
  {
    path: '/',
    name: 'Home',
    component: HomeView
  },
  {
    path: '/article/:id',
    name: 'ArticleDetail',
    component: ArticleView,
    props: true
  },
  {
    path: '/article/new',
    name: 'NewArticle',
    component: ArticleForm
  },
  {
    path: '/article/edit/:id',
    name: 'EditArticle',
    component: ArticleForm,
    props: true
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;