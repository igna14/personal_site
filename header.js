// Load header component
async function loadHeader() {
  try {
    const response = await fetch('header.html');
    const headerHTML = await response.text();
    document.getElementById('header-placeholder').outerHTML = headerHTML;
  } catch (error) {
    console.error('Error loading header:', error);
  }
}

// Load header when DOM is ready
if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', loadHeader);
} else {
  loadHeader();
}