// src/components/ResultsList.jsx
import React from 'react';
import styles from './ResultsList.module.css';

function ResultsList({ results }) {
  const safeResults = Array.isArray(results) ? results : [];

  return (
    <div className={styles.resultsList}>
      {safeResults.length === 0 ? (
        <p>No results.</p>
      ) : (
        safeResults.map((item, index) => (
          <div key={index} className={styles.resultItem}>
            {item}
          </div>
        ))
      )}
    </div>
  );
}

export default ResultsList;