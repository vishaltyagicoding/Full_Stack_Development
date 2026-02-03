// Main Application
class StudentsTable {
    constructor() {
        this.currentPage = 1;
        this.rowsPerPage = 10;
        this.sortColumn = null;
        this.sortDirection = 'asc';
        this.searchTerm = '';
        this.filterCity = '';
        this.studentToDelete = null;
        
        this.init();
    }
    
    init() {
        this.updateCurrentTime();
        this.setupEventListeners();
        this.updatePagination();
        this.setupRealTimeClock();
    }
    
    setupEventListeners() {
        // Export to CSV
        document.getElementById('exportCSV').addEventListener('click', () => this.exportToCSV());
        
        // Print table
        document.getElementById('printTable').addEventListener('click', () => window.print());
        
        // Refresh data
        document.getElementById('refreshData').addEventListener('click', () => this.refreshData());
        
        // Search functionality
        const searchInput = document.getElementById('searchInput');
        searchInput.addEventListener('input', (e) => {
            this.searchTerm = e.target.value.toLowerCase();
            this.filterTable();
        });
        
        document.getElementById('clearSearch').addEventListener('click', () => {
            searchInput.value = '';
            this.searchTerm = '';
            this.filterTable();
        });
        
        // Filter by city
        document.getElementById('filterCity').addEventListener('change', (e) => {
            this.filterCity = e.target.value.toLowerCase();
            this.filterTable();
        });
        
        // Sort by
        document.getElementById('sortBy').addEventListener('change', (e) => {
            this.sortColumn = e.target.value;
            this.sortTable();
        });
        
        // Rows per page
        document.getElementById('rowsPerPage').addEventListener('change', (e) => {
            this.rowsPerPage = parseInt(e.target.value);
            this.currentPage = 1;
            this.updatePagination();
        });
        
        // Pagination buttons
        document.getElementById('prevPage').addEventListener('click', () => this.prevPage());
        document.getElementById('nextPage').addEventListener('click', () => this.nextPage());
        
        // Table header click for sorting
        document.querySelectorAll('.students-table th[data-sort]').forEach(th => {
            th.addEventListener('click', () => {
                const column = th.getAttribute('data-sort');
                this.sortByColumn(column);
            });
        });
        
        // Action buttons
        document.addEventListener('click', (e) => {
            if (e.target.closest('.view-btn')) {
                const studentId = e.target.closest('.view-btn').getAttribute('data-id');
                this.viewStudentDetails(studentId);
            }
            
            if (e.target.closest('.edit-btn')) {
                const studentId = e.target.closest('.edit-btn').getAttribute('data-id');
                this.editStudent(studentId);
            }
            
            if (e.target.closest('.delete-btn')) {
                const studentId = e.target.closest('.delete-btn').getAttribute('data-id');
                this.confirmDelete(studentId);
            }
        });
        
        // Modal close buttons
        document.querySelectorAll('.close-modal').forEach(btn => {
            btn.addEventListener('click', () => this.closeModal(btn.closest('.modal')));
        });
        
        document.querySelectorAll('.modal').forEach(modal => {
            modal.addEventListener('click', (e) => {
                if (e.target === modal) {
                    this.closeModal(modal);
                }
            });
        });
        
        // Confirmation modal
        document.getElementById('cancelAction').addEventListener('click', () => {
            this.closeModal(document.getElementById('confirmModal'));
        });
        
        document.getElementById('confirmAction').addEventListener('click', () => {
            this.deleteStudent();
        });
        
        // Keyboard shortcuts
        document.addEventListener('keydown', (e) => {
            if (e.key === 'Escape') {
                document.querySelectorAll('.modal').forEach(modal => {
                    this.closeModal(modal);
                });
            }
            
            if (e.ctrlKey && e.key === 'f') {
                e.preventDefault();
                document.getElementById('searchInput').focus();
            }
            
            if (e.key === 'Enter' && document.activeElement.id === 'searchInput') {
                this.filterTable();
            }
        });
    }
    
    updateCurrentTime() {
        const now = new Date();
        const options = { 
            weekday: 'long', 
            year: 'numeric', 
            month: 'long', 
            day: 'numeric',
            hour: '2-digit',
            minute: '2-digit',
            second: '2-digit'
        };
        document.getElementById('currentTime').textContent = now.toLocaleDateString('en-US', options);
    }
    
    setupRealTimeClock() {
        setInterval(() => this.updateCurrentTime(), 1000);
    }
    
    filterTable() {
        const rows = document.querySelectorAll('#tableBody tr:not(.empty-message)');
        let visibleCount = 0;
        
        rows.forEach(row => {
            const city = row.getAttribute('data-city') || '';
            const text = row.textContent.toLowerCase();
            const matchesSearch = !this.searchTerm || text.includes(this.searchTerm);
            const matchesCity = !this.filterCity || city.includes(this.filterCity);
            
            if (matchesSearch && matchesCity) {
                row.style.display = '';
                visibleCount++;
            } else {
                row.style.display = 'none';
            }
        });
        
        this.updateRecordsInfo(visibleCount);
        this.updatePagination();
    }
    
    sortByColumn(column) {
        // Update sort icons
        document.querySelectorAll('.students-table th').forEach(th => {
            th.classList.remove('sorted-asc', 'sorted-desc');
        });
        
        const th = document.querySelector(`.students-table th[data-sort="${column}"]`);
        const isAsc = this.sortColumn === column && this.sortDirection === 'asc';
        this.sortDirection = isAsc ? 'desc' : 'asc';
        this.sortColumn = column;
        
        th.classList.add(this.sortDirection === 'asc' ? 'sorted-asc' : 'sorted-desc');
        
        this.sortTable();
    }
    
    sortTable() {
        const rows = Array.from(document.querySelectorAll('#tableBody tr:not(.empty-message)'));
        const tbody = document.getElementById('tableBody');
        
        rows.sort((a, b) => {
            let aValue, bValue;
            
            switch(this.sortColumn) {
                case 'id':
                    aValue = parseInt(a.querySelector('.id-cell').textContent);
                    bValue = parseInt(b.querySelector('.id-cell').textContent);
                    break;
                case 'name':
                    aValue = a.querySelector('.name-cell').textContent.toLowerCase();
                    bValue = b.querySelector('.name-cell').textContent.toLowerCase();
                    break;
                case 'age':
                    aValue = parseInt(a.querySelector('.age-badge').textContent);
                    bValue = parseInt(b.querySelector('.age-badge').textContent);
                    break;
                case 'email':
                    aValue = a.querySelector('.email-cell a').textContent.toLowerCase();
                    bValue = b.querySelector('.email-cell a').textContent.toLowerCase();
                    break;
                case 'date':
                    aValue = new Date(a.querySelector('.date-cell').getAttribute('data-date'));
                    bValue = new Date(b.querySelector('.date-cell').getAttribute('data-date'));
                    break;
                case 'city':
                    aValue = a.querySelector('.city-cell').textContent.toLowerCase();
                    bValue = b.querySelector('.city-cell').textContent.toLowerCase();
                    break;
                default:
                    return 0;
            }
            
            if (this.sortDirection === 'asc') {
                return aValue > bValue ? 1 : -1;
            } else {
                return aValue < bValue ? 1 : -1;
            }
        });
        
        // Reorder rows
        rows.forEach(row => tbody.appendChild(row));
    }
    
    updatePagination() {
        const rows = document.querySelectorAll('#tableBody tr:not(.empty-message)');
        const totalRows = Array.from(rows).filter(row => row.style.display !== 'none').length;
        const totalPages = Math.ceil(totalRows / this.rowsPerPage);
        
        // Update current page if needed
        if (this.currentPage > totalPages && totalPages > 0) {
            this.currentPage = totalPages;
        }
        
        // Update buttons
        document.getElementById('prevPage').disabled = this.currentPage === 1;
        document.getElementById('nextPage').disabled = this.currentPage === totalPages || totalPages === 0;
        
        // Update page info
        document.getElementById('pageInfo').textContent = 
            totalPages > 0 ? `Page ${this.currentPage} of ${totalPages}` : 'No records';
        
        // Show/hide rows based on pagination
        let startIndex = (this.currentPage - 1) * this.rowsPerPage;
        let endIndex = startIndex + this.rowsPerPage;
        let visibleIndex = 0;
        
        rows.forEach((row, index) => {
            if (row.style.display !== 'none') {
                if (visibleIndex >= startIndex && visibleIndex < endIndex) {
                    row.style.display = '';
                } else {
                    row.style.display = 'none';
                }
                visibleIndex++;
            }
        });
        
        this.updateRecordsInfo(totalRows);
    }
    
    prevPage() {
        if (this.currentPage > 1) {
            this.currentPage--;
            this.updatePagination();
        }
    }
    
    nextPage() {
        const rows = document.querySelectorAll('#tableBody tr:not(.empty-message)');
        const totalRows = Array.from(rows).filter(row => row.style.display !== 'none').length;
        const totalPages = Math.ceil(totalRows / this.rowsPerPage);
        
        if (this.currentPage < totalPages) {
            this.currentPage++;
            this.updatePagination();
        }
    }
    
    updateRecordsInfo(totalRows) {
        const start = Math.min((this.currentPage - 1) * this.rowsPerPage + 1, totalRows);
        const end = Math.min(this.currentPage * this.rowsPerPage, totalRows);
        
        let infoText = '';
        if (totalRows === 0) {
            infoText = 'No records found';
        } else if (this.rowsPerPage >= totalRows) {
            infoText = `Showing ${totalRows} records`;
        } else {
            infoText = `Showing ${start} to ${end} of ${totalRows} records`;
        }
        
        document.getElementById('recordsInfo').textContent = infoText;
    }
    
    showLoading() {
        document.getElementById('loadingSpinner').style.display = 'block';
    }
    
    hideLoading() {
        document.getElementById('loadingSpinner').style.display = 'none';
    }
    
    showModal(modalId) {
        const modal = document.getElementById(modalId);
        modal.style.display = 'block';
        document.body.style.overflow = 'hidden';
    }
    
    closeModal(modal) {
        if (modal) {
            modal.style.display = 'none';
            document.body.style.overflow = 'auto';
        }
    }
    
    viewStudentDetails(studentId) {
        const row = document.querySelector(`tr[data-id="${studentId}"]`);
        if (!row) {
            alert('Student not found!');
            return;
        }
        
        const details = {
            'ID': row.querySelector('.id-cell').textContent,
            'Name': row.querySelector('.name-cell').textContent.replace(/^\s*[^a-zA-Z]*/, '').trim(),
            'Age': row.querySelector('.age-badge').textContent + ' years',
            'Email': row.querySelector('.email-cell a').textContent,
            'Enrollment Date': row.querySelector('.date-cell').textContent.replace(/^\s*[^a-zA-Z]*/, '').trim(),
            'City': row.querySelector('.city-cell').textContent.replace(/^\s*[^a-zA-Z]*/, '').trim()
        };
        
        let modalHTML = '';
        for (const [label, value] of Object.entries(details)) {
            modalHTML += `
                <div class="student-detail">
                    <span class="detail-label">${label}:</span>
                    <span class="detail-value">${value}</span>
                </div>
            `;
        }
        
        document.getElementById('modalBody').innerHTML = modalHTML;
        this.showModal('viewModal');
    }
    
    editStudent(studentId) {
        alert(`Edit functionality for student ID: ${studentId}\nThis would typically open an edit form.`);
    }
    
    confirmDelete(studentId) {
        this.studentToDelete = studentId;
        const studentName = document.querySelector(`tr[data-id="${studentId}"] .name-cell`).textContent
            .replace(/^\s*[^a-zA-Z]*/, '').trim();
        
        document.getElementById('confirmMessage').innerHTML = `
            <p>Are you sure you want to delete student:</p>
            <p><strong>${studentName} (ID: ${studentId})</strong>?</p>
            <p class="warning-text"><i class="fas fa-exclamation-circle"></i> This action cannot be undone!</p>
        `;
        
        this.showModal('confirmModal');
    }
    
    deleteStudent() {
        if (!this.studentToDelete) return;
        
        this.showLoading();
        
        // Simulate API call
        setTimeout(() => {
            const row = document.querySelector(`tr[data-id="${this.studentToDelete}"]`);
            if (row) {
                row.style.transition = 'all 0.5s ease';
                row.style.opacity = '0';
                row.style.transform = 'translateX(-100%)';
                
                setTimeout(() => {
                    row.remove();
                    this.updatePagination();
                    this.showNotification(`Student ID ${this.studentToDelete} deleted successfully!`, 'success');
                }, 500);
            }
            
            this.hideLoading();
            this.closeModal(document.getElementById('confirmModal'));
            this.studentToDelete = null;
        }, 1000);
    }
    
    refreshData() {
        this.showLoading();
        
        // Simulate data refresh
        setTimeout(() => {
            this.filterTable();
            this.sortTable();
            this.hideLoading();
            this.showNotification('Data refreshed successfully!', 'info');
        }, 800);
    }
    
    exportToCSV() {
        const rows = document.querySelectorAll('#tableBody tr:not(.empty-message)');
        if (rows.length === 0) {
            alert('No data to export!');
            return;
        }
        
        let csv = [];
        let headers = [];
        
        // Get headers (excluding Actions column)
        document.querySelectorAll('thead th').forEach((th, index) => {
            if (index < 6) { // Only first 6 columns (excluding Actions)
                const headerText = th.textContent.trim()
                    .replace(/\n/g, ' ')
                    .replace(/\s+/g, ' ');
                headers.push(headerText);
            }
        });
        csv.push(headers.join(','));
        
        // Get rows data
        rows.forEach(row => {
            if (row.style.display !== 'none') {
                let rowData = [];
                const cells = row.querySelectorAll('td');
                
                cells.forEach((cell, index) => {
                    if (index < 6) { // Only first 6 columns (excluding Actions)
                        let text = cell.textContent.trim()
                            .replace(/\n/g, ' ')
                            .replace(/\s+/g, ' ')
                            .replace(/years$/, '')
                            .trim();
                        rowData.push('"' + text + '"');
                    }
                });
                
                csv.push(rowData.join(','));
            }
        });
        
        // Create and download CSV file
        const csvContent = "data:text/csv;charset=utf-8," + csv.join('\n');
        const encodedUri = encodeURI(csvContent);
        const link = document.createElement("a");
        link.setAttribute("href", encodedUri);
        link.setAttribute("download", `students_${new Date().toISOString().slice(0,10)}.csv`);
        document.body.appendChild(link);
        link.click();
        document.body.removeChild(link);
        
        this.showNotification('CSV exported successfully!', 'success');
    }
    
    showNotification(message, type = 'info') {
        // Remove existing notifications
        const existingNotifications = document.querySelectorAll('.notification');
        existingNotifications.forEach(notif => notif.remove());
        
        // Create notification
        const notification = document.createElement('div');
        notification.className = `notification notification-${type}`;
        notification.innerHTML = `
            <i class="fas fa-${type === 'success' ? 'check-circle' : type === 'error' ? 'exclamation-circle' : 'info-circle'}"></i>
            <span>${message}</span>
            <button class="notification-close"><i class="fas fa-times"></i></button>
        `;
        
        document.body.appendChild(notification);
        
        // Show with animation
        setTimeout(() => {
            notification.classList.add('show');
        }, 10);
        
        // Auto remove after 3 seconds
        setTimeout(() => {
            notification.classList.remove('show');
            setTimeout(() => notification.remove(), 300);
        }, 3000);
        
        // Close button
        notification.querySelector('.notification-close').addEventListener('click', () => {
            notification.classList.remove('show');
            setTimeout(() => notification.remove(), 300);
        });
    }
}

// Add notification styles dynamically
const notificationStyles = document.createElement('style');
notificationStyles.textContent = `
    .notification {
        position: fixed;
        top: 20px;
        right: 20px;
        padding: 15px 25px;
        border-radius: 10px;
        color: white;
        font-weight: 500;
        display: flex;
        align-items: center;
        gap: 15px;
        z-index: 10000;
        box-shadow: 0 5px 20px rgba(0,0,0,0.15);
        transform: translateX(100%);
        opacity: 0;
        transition: transform 0.3s ease, opacity 0.3s ease;
        min-width: 300px;
        max-width: 400px;
    }
    
    .notification.show {
        transform: translateX(0);
        opacity: 1;
    }
    
    .notification-success {
        background: linear-gradient(135deg, #2ecc71, #27ae60);
        border-left: 5px solid #27ae60;
    }
    
    .notification-info {
        background: linear-gradient(135deg, #3498db, #2980b9);
        border-left: 5px solid #2980b9;
    }
    
    .notification-error {
        background: linear-gradient(135deg, #e74c3c, #c0392b);
        border-left: 5px solid #c0392b;
    }
    
    .notification i {
        font-size: 1.3rem;
    }
    
    .notification-close {
        background: none;
        border: none;
        color: white;
        cursor: pointer;
        padding: 5px;
        margin-left: auto;
        opacity: 0.8;
        transition: opacity 0.3s;
    }
    
    .notification-close:hover {
        opacity: 1;
    }
`;
document.head.appendChild(notificationStyles);

// Initialize the application when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
    window.studentsTable = new StudentsTable();
});

// Add warning text style
const warningStyles = document.createElement('style');
warningStyles.textContent = `
    .warning-text {
        color: #e74c3c;
        font-weight: 600;
        margin-top: 10px;
        display: flex;
        align-items: center;
        gap: 10px;
        background: rgba(231, 76, 60, 0.1);
        padding: 10px;
        border-radius: 8px;
        border-left: 4px solid #e74c3c;
    }
    
    .warning-text i {
        color: #e74c3c;
    }
`;
document.head.appendChild(warningStyles);