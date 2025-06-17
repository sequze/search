import React from 'react';
import styles from './Pagination.module.css';

function Pagination({ page, setPage, hasNext }) {
  return (
    <div className={styles.pagination}>
      <button disabled={page === 1} onClick={() => setPage(page - 1)}>
        Prev
      </button>
      <span>Page {page}</span>
      <button disabled={!hasNext} onClick={() => setPage(page + 1)}>
        Next
      </button>
    </div>
  );
}

export default Pagination;