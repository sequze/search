import axios from 'axios';

const API_BASE = 'http://localhost:8000';

export const loginUser = async (username, password) => {
  const params = new URLSearchParams();
  params.append('username', username);
  params.append('password', password);

  const res = await axios.post(`${API_BASE}/auth/jwt/login`, params);
  return res.data.access_token;
};

export const searchRequest = async (token, searchQuery, page = 1) => {
  const res = await axios.get(`${API_BASE}/search/request`, {
    headers: { Authorization: `Bearer ${token}` },
    params: { request: searchQuery, page },
  });
  return res.data;
  
};
