document.addEventListener('DOMContentLoaded', function() {

    // --- Gestion Année Copyright ---
    function updateCopyrightYear() {
      const yearSpan = document.getElementById('currentYear') || document.getElementById('currentYearPortfolio') || document.getElementById('currentYearContact');
      if (yearSpan) {
        yearSpan.textContent = new Date().getFullYear();
      }
    }
    updateCopyrightYear(); // Met à jour au chargement initial

    // --- Filtre Portfolio ---
    const filterContainer = document.querySelector('.portfolio-filters');
    const portfolioGrid = document.querySelector('.portfolio-grid');
    const portfolioItems = portfolioGrid ? portfolioGrid.querySelectorAll('.portfolio-item') : []; // Vérifie si portfolioGrid existe

    if (filterContainer && portfolioItems.length > 0) {
        filterContainer.addEventListener('click', function(e) {
            if (e.target.tagName === 'BUTTON') {
                // Gestion du bouton actif
                const currentActiveButton = filterContainer.querySelector('.active');
                if (currentActiveButton) {
                    currentActiveButton.classList.remove('active');
                }
                e.target.classList.add('active');

                const filterValue = e.target.getAttribute('data-filter');

                portfolioItems.forEach(item => {
                    const itemCategories = item.getAttribute('data-category').split(' '); // Gère plusieurs catégories par item
                    const shouldShow = filterValue === 'all' || itemCategories.includes(filterValue);

                    // Ajoute/retire classes pour animation
                    if (shouldShow) {
                        item.classList.remove('hide');
                        item.classList.add('show');
                    } else {
                        item.classList.remove('show');
                        item.classList.add('hide');
                    }

                    // Alternative sans animation (plus simple) :
                    // item.style.display = shouldShow ? 'block' : 'none';
                });
            }
        });
    }

    // --- Remplissage dynamique de la Modale Portfolio ---
    const portfolioModal = document.getElementById('portfolioModal');
    if (portfolioModal) {
        portfolioModal.addEventListener('show.bs.modal', function (event) {
            // Bouton qui a déclenché la modale
            const button = event.relatedTarget;

            // Extraire les informations des attributs data-*
            const title = button.getAttribute('data-title');
            const imgSrc = button.getAttribute('data-img');
            const description = button.getAttribute('data-desc');
            const technologies = button.getAttribute('data-tech');
            const testimonial = button.getAttribute('data-testimonial');

            // Mettre à jour le contenu de la modale
            const modalTitle = portfolioModal.querySelector('.modal-title');
            const modalImage = portfolioModal.querySelector('#modalProjectImage');
            const modalDesc = portfolioModal.querySelector('#modalProjectDesc');
            const modalTech = portfolioModal.querySelector('#modalProjectTech');
            const modalTestimonial = portfolioModal.querySelector('#modalProjectTestimonial');

            modalTitle.textContent = title;
            modalImage.src = imgSrc;
            modalImage.alt = "Détail du projet " + title; // Met à jour l'alt pour l'accessibilité
            modalDesc.textContent = description;
            modalTech.textContent = technologies;

            const testimonialBlock = modalTestimonial.closest('blockquote');
            if (testimonial && testimonial !== "") {
                 modalTestimonial.innerHTML = testimonial; // Utilise innerHTML pour interpréter les "
                 testimonialBlock.style.display = 'block'; // Affiche le bloc témoignage
            } else {
                 testimonialBlock.style.display = 'none'; // Cache le bloc si pas de témoignage
            }
        });
    }

    // --- Optionnel : Navbar qui change de style au scroll ---
    const navbar = document.querySelector('.navbar-custom');
    if (navbar && navbar.classList.contains('fixed-top')) { // Appliquer seulement si navbar est fixe
        const heroSectionHeight = document.querySelector('.hero-section') ? document.querySelector('.hero-section').offsetHeight : 100; // Hauteur approximative
        window.addEventListener('scroll', function() {
            if (window.scrollY > 50) { // Devient opaque après 50px de scroll
                navbar.style.backgroundColor = 'var(--secondary-color)'; // Ou #2A3F54 directement
            } else {
                navbar.style.backgroundColor = 'rgba(42, 63, 84, 0.95)'; // Retourne à la transparence
            }
        });
    }

});
