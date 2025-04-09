document.addEventListener('DOMContentLoaded', () => {
    const itemList = document.getElementById('item-list');

    function fetchItems() {
        itemList.innerHTML = '<li class="loading">Loading items...</li>';
        fetch('https://my-elegant-app-1.onrender.com')
            .then(response => {
                if (!response.ok) {
                    throw new Error(`HTTP error! status: ${response.status}`);
                }
                return response.json();
            })
            .then(data => {
                itemList.innerHTML = ''; // Clear loading message
                if (data.length > 0) {
                    data.forEach(item => {
                        const listItem = document.createElement('li');
                        listItem.innerHTML = `<strong>${item.name}:</strong> ${item.description} (ID: ${item.id})`;
                        itemList.appendChild(listItem);
                    });
                } else {
                    itemList.innerHTML = '<li class="empty">No items available.</li>';
                }
            })
            .catch(error => {
                console.error('Error fetching items:', error);
                itemList.innerHTML = '<li class="error">Failed to load items. Please try again later.</li>';
            });
    }

    // Initial fetch of items when the page loads
    fetchItems();
});
