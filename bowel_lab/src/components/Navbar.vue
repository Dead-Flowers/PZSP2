<template>
    <div class="navbar">
        <div class="navbar-start">
            <label class="page-name">Bowel Lab</label>
            <div class="tab-space">
                <input 
                class="tab input-element-standard"
                type="button"
                value="Nowa Analiza"
                />
                <input 
                class="tab input-element-standard"
                type="button"
                value="Pacjenci"
                />
                <input 
                class="tab input-element-standard"
                type="button"
                value="Wyniki"
                />
                <!-- future tabs-->
            </div>
        </div>
        
        <div class="navbar-end">
            <input 
                class="input-element-standard"
                type="button"
                value="Wyloguj"
            />
        </div>
    </div>
</template>

<script>
export default {
    name: 'Navbar'
}
</script>

<style>
.navbar {
    top: 0;
    position: fixed;
    z-index: 10;
    background-color: var(--color-navbar);
    margin: 0;
    padding-block-start: 40px;
    height: 100vh;
    width: 10vw;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: space-between;
    overflow-x: hidden;
}

.page-name {
    font-size: 1.5rem;
    margin-inline: 15px;
    margin-block-end: 40px;
}

.tab-space {
    display: flex;
    flex-direction: column;
    justify-content: space-between;
}

.tab {
    background-color: #444444 !important;
    opacity: 0.8;
    margin-block-end: 3px !important;
    border: 0 !important;
    border-radius: 0 !important;
    padding-block: 15px;
    width: 10vw;
    font-family: "Balsamiq Sans", cursive;
    color: var(--color-text);
}

.input-element-standard {
    background-color: var(--color-accent);
    border: 0;
    border-radius: 3px;
    padding: 20px;
    font-size: 1rem;
    margin-block-end: 60px;
}

.input-element-standard:hover{
    filter: brightness(85%);
} 
</style>