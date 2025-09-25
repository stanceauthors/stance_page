// STANCE Website JavaScript

// Mobile warning functionality
function dismissWarning() {
    const warning = document.getElementById('mobile-warning');
    if (warning) {
        warning.style.display = 'none';
    }
}

// Smooth scrolling for navigation links
document.addEventListener('DOMContentLoaded', function() {
    // Handle navigation links
    const navLinks = document.querySelectorAll('.nav-link');
    
    navLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            
            const targetId = this.getAttribute('href').substring(1);
            const targetSection = document.getElementById(targetId);
            
            if (targetSection) {
                targetSection.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
                
                // Update active navigation
                navLinks.forEach(l => l.classList.remove('active'));
                this.classList.add('active');
            }
        });
    });
    
    // Video lazy loading and error handling
    const videos = document.querySelectorAll('video');
    
    videos.forEach(video => {
        // Ensure autoplay compatibility
        video.muted = true;
        video.setAttribute('muted', '');
        video.playsInline = true;
        video.setAttribute('playsinline', '');
        video.autoplay = true;
        video.setAttribute('autoplay', '');
        
        // Add loading state
        video.addEventListener('loadstart', function() {
            this.style.opacity = '0.5';
        });
        
        // Remove loading state when ready
        video.addEventListener('canplay', function() {
            this.style.opacity = '1';
        });
        
        // Handle video errors
        video.addEventListener('error', function() {
            console.error('Video failed to load:', this.src);
            this.style.border = '2px solid #dc3545';
            
            // Create error message
            const errorDiv = document.createElement('div');
            errorDiv.className = 'video-error';
            errorDiv.innerHTML = '<i class="fas fa-exclamation-triangle"></i> Video failed to load';
            errorDiv.style.cssText = `
                position: absolute;
                top: 50%;
                left: 50%;
                transform: translate(-50%, -50%);
                background: rgba(220, 53, 69, 0.9);
                color: white;
                padding: 10px;
                border-radius: 5px;
                font-size: 14px;
                text-align: center;
            `;
            
            this.parentElement.style.position = 'relative';
            this.parentElement.appendChild(errorDiv);
        });
        
        // Intersection Observer for lazy loading
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    const video = entry.target;
                    video.load(); // Start loading the video
                    // Attempt autoplay when entering viewport
                    const playPromise = video.play();
                    if (playPromise && typeof playPromise.then === 'function') {
                        playPromise.catch(() => {});
                    }
                    observer.unobserve(video);
                }
            });
        }, {
            threshold: 0.1
        });
        
        observer.observe(video);
    });
    
    // Image error handling
    const images = document.querySelectorAll('img');
    
    images.forEach(img => {
        img.addEventListener('error', function() {
            console.error('Image failed to load:', this.src);
            this.style.border = '2px solid #dc3545';
            this.alt = 'Image failed to load';
            
            // Create placeholder
            const placeholder = document.createElement('div');
            placeholder.className = 'image-placeholder';
            placeholder.innerHTML = '<i class="fas fa-image"></i><br>Image not found';
            placeholder.style.cssText = `
                width: ${this.width || 280}px;
                height: ${this.height || 280}px;
                background: #f8f9fa;
                border: 2px dashed #6c757d;
                display: flex;
                flex-direction: column;
                justify-content: center;
                align-items: center;
                color: #6c757d;
                font-size: 14px;
                text-align: center;
                border-radius: 8px;
            `;
            
            this.parentElement.insertBefore(placeholder, this);
            this.style.display = 'none';
    });
});

    // Highlight active section in navigation
    const sections = document.querySelectorAll('.main-section');
    
    const observerOptions = {
        threshold: 0.3,
        rootMargin: '-50px 0px -50px 0px'
    };
    
    const sectionObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const sectionId = entry.target.id;
                
                // Update navigation
                navLinks.forEach(link => {
                    link.classList.remove('active');
                    if (link.getAttribute('href') === `#${sectionId}`) {
                        link.classList.add('active');
                    }
                });
            }
        });
    }, observerOptions);
    
    sections.forEach(section => {
        sectionObserver.observe(section);
    });
    
    // Mobile sidebar toggle (if needed)
    function createMobileToggle() {
        if (window.innerWidth <= 768) {
            const toggleBtn = document.createElement('button');
            toggleBtn.innerHTML = '<i class="fas fa-bars"></i>';
            toggleBtn.className = 'mobile-toggle';
            toggleBtn.style.cssText = `
                position: fixed;
                top: 20px;
                left: 20px;
                z-index: 1001;
                background: #667eea;
                color: white;
                border: none;
                border-radius: 5px;
                padding: 10px;
                font-size: 18px;
                cursor: pointer;
                box-shadow: 0 2px 10px rgba(0,0,0,0.3);
            `;
            
            toggleBtn.addEventListener('click', function() {
                const sidebar = document.querySelector('.sidebar');
                sidebar.classList.toggle('active');
            });
            
            document.body.appendChild(toggleBtn);
        }
    }
    
    createMobileToggle();
    
    // Re-create mobile toggle on window resize
    window.addEventListener('resize', function() {
        const existingToggle = document.querySelector('.mobile-toggle');
        if (existingToggle) {
            existingToggle.remove();
        }
        createMobileToggle();
    });
    
    // Close mobile sidebar when clicking outside
    document.addEventListener('click', function(e) {
        const sidebar = document.querySelector('.sidebar');
        const mobileToggle = document.querySelector('.mobile-toggle');
        
        if (window.innerWidth <= 768 && 
            sidebar.classList.contains('active') && 
            !sidebar.contains(e.target) && 
            !mobileToggle.contains(e.target)) {
            sidebar.classList.remove('active');
        }
    });
    
    console.log('STANCE website initialized successfully!');
});