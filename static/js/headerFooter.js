function cargarContenido(url, contenedorId) {
    fetch(url)
      .then(response => response.text())
      .then(data => {
        document.getElementById(contenedorId).innerHTML = data;
      });
  }
 
  cargarContenido('./header.html', 'header-nav-container');
  cargarContenido('./footer.html', 'footer-container');