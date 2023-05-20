<template>
    <nav class="navbar navbar-expand-lg bg-dark-theme1">
      <div class="container-fluid">
        <a class="navbar-brand text-light" href="#">Dictionary</a>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarSupportedContent">
          <ul class="navbar-nav me-auto mb-2 mb-lg-0">
            <li class="nav-item">
              <a class="nav-link active text-white" aria-current="page" href="#">Home</a>
            </li>
            <li class="nav-item">
              <a class="nav-link text-light" href="#">About</a>
            </li>
          </ul>
        </div>
      </div>
    </nav>
</template>

<script>
export default ({
    name: 'NavBarComponent',
})
</script>

<style></style>