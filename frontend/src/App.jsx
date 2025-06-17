import React, { useState, useEffect } from 'react';
import { loginUser, searchRequest } from './api';
import LoginForm from './components/LoginForm';
import SearchInterface from './components/SearchInterface';
import ResultsList from './components/ResultsList';
import Pagination from './components/Pagination';
import styles from './App.module.css';

function App() {
  const [token, setToken] = useState(localStorage.getItem('token') || '');
  const [searchQuery, setSearchQuery] = useState('');
  const [results, setResults] = useState([]);
  const [page, setPage] = useState(1);
  const [hasNext, setHasNext] = useState(false);

  const handleLogin = async (username, password) => {
    try {
      const newToken = await loginUser(username, password);
      setToken(newToken);
      localStorage.setItem('token', newToken);
    } catch {
      alert('Login failed');
    }
  };

  const handleLogout = () => {
    setToken('');
    localStorage.removeItem('token');
    setResults([]);
    setSearchQuery('');
    setPage(1);
  };

  const handleSearch = async () => {
    if (!searchQuery) return;
    try {
      const data = await searchRequest(token, searchQuery, page);
      setResults(data.results);
      setHasNext(data.has_next);
    } catch {
      alert('Search failed');
    }
  };

  useEffect(() => {
    if (token && searchQuery) {
      handleSearch();
    }
  }, [page]);

  return (
    <div className={styles.app}>
      {!token ? (
        <LoginForm onLogin={handleLogin} />
      ) : (
        <>
          <SearchInterface
            searchQuery={searchQuery}
            setSearchQuery={setSearchQuery}
            onSearch={handleSearch}
            onLogout={handleLogout}
          />
          <ResultsList results={results} />
          <Pagination page={page} setPage={setPage} hasNext={hasNext} />
        </>
      )}
    </div>
  );
}

export default App;
