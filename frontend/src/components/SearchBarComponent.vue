<template>
    <div class="row mb-3">
        <div class="col-6">
            <label for="exampleInputEmail1" class="form-label">Base</label>
            <select class="form-select" aria-label="Default select example">
                <option selected>English</option>
                <option value="1">One</option>
            </select>
        </div>
        <div class="col-6">
            <label for="exampleInputEmail1" class="form-label">Secondary</label>
            <select class="form-select" aria-label="Default select example">
                <option selected>Bengali</option>
                <option value="1">One</option>
            </select>
        </div>
    </div>
    <div class="mb-3">
        <input type="email" class="form-control" aria-describedby="emailHelp" placeholder="Type your word here...">
        <div id="emailHelp" class="form-text">When you will stop typing the result will be shown in below.</div>
    </div>
</template>

<script>
export default ({
    name: 'SearchBarComponent',
})
</script>