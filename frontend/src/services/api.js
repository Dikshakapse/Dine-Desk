import axios from 'axios';

const api = axios.create({
  baseURL: 'http://localhost:8000/api/', // Update with your backend URL
});

export const login = (credentials) => api.post('users/login/', credentials);
export const register = (data) => api.post('users/register/', data);
export const getDashboardData = () => api.get('dashboard/');
export const getMenu = () => api.get('daily-menus/');
export const placeOrder = (orderData) => api.post('orders/', orderData);
export const getBilling = () => api.get('billings/');
export const submitFeedback = (feedbackData) => api.post('feedbacks/', feedbackData);
export const trackDelivery = (orderId) => api.get(`delivery-tracking/${orderId}/`);
export const getUserProfile = () => api.get('user-profiles/');

export default api;
