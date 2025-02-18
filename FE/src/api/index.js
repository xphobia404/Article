import axios from 'axios';

const API_URL = 'http://localhost:5000/';

const api = axios.create({
  baseURL: API_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

export const getArticles = async (limit = 10, offset = 0) => {
  try {
    const response = await api.get(`article/?limit=${limit}&offset=${offset}`);
    return response.data;
  } catch (error) {
    console.error('Error fetching articles:', error);
    throw error;
  }
};

export const getArticleById = async (id) => {
  try {
    const response = await api.get(`article/${id}`);
    return response.data;
  } catch (error) {
    console.error('Error fetching article:', error);
    throw error;
  }
};

export const createArticle = async (articleData) => {
  try {
    const response = await api.post('article', articleData);
    return response.data;
  } catch (error) {
    console.error('Error creating article:', error);
    throw error;
  }
};

export const updateArticle = async (articleData) => {
  try {
    const response = await api.post('article/update', articleData);
    return response.data;
  } catch (error) {
    console.error('Error updating article:', error);
    throw error;
  }
};

export const deleteArticle = async (id) => {
  try {
    const response = await api.post('article/delete', { id });
    return response.data;
  } catch (error) {
    console.error('Error deleting article:', error);
    throw error;
  }
};

export default api;