// src/components/SearchInterface.jsx
import React from 'react';
import styles from './SearchPanel.module.css';

function SearchInterface({
  searchQuery,
  setSearchQuery,
  onSearch,
  onLogout,
}) {
  return (
    <div className={styles.searchInterface}>
      <input
        type="text"
        placeholder="Search..."
        value={searchQuery}
        onChange={(e) => setSearchQuery(e.target.value)}
      />
      <button onClick={onSearch}>Search</button>
      <button onClick={onLogout}>Logout</button>
    </div>
  );
}

export default SearchInterface;