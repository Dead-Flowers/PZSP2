<template>
  <form class="analysis-init-container">
    <input
      class="input-element-standard"
      type="button"
      value="Rozpocznij Analizę"
    />
    <input
      class="input-element-standard keyboard-input"
      type="number"
      name="patient-id" 
      placeholder="Numer identyfikacyjny pacjenta..."
      autocomplete="off"
    />
    <input
      class="input-file-field"
      type="file"
      name="bowel-sound-file"
      accept=".mp3"
    />
  </form>
</template>

<script>

export default {
  name: "AnalysisInit"
}
</script>

<style scoped>
.input-element-standard, .input-file-field::-webkit-file-upload-button {
  background-color: var(--color-accent);
  margin-inline-start: 20px;
  border: none;
  border-radius: 3px;
  padding-block: 10px;
  padding-inline: 15px;
  font-family:  "Roboto", sans-serif;
  color: var(--color-text);
}

.input-element-standard:hover, .input-file-field::-webkit-file-upload-button:hover {
    filter: brightness(95%);
}

.keyboard-input:focus {
  outline: none;
}

.keyboard-input::placeholder {
  color: var(--color-text-darker);
  opacity: 1; 
}

.keyboard-input:-ms-input-placeholder {
  color: var(--color-text-darker);
}

.keyboard-input::-webkit-inner-spin-button, 
.keyboard-input::-webkit-outer-spin-button { 
  -webkit-appearance: none; 
  margin: 0; 
}

.button {
  margin-block-start: 10px !important;
  font-size: 1rem;  
}

.link {
  background-color: transparent !important;
  text-decoration: none;
  font-size: 0.8rem !important;
}

.link:hover {
  filter: brightness(95%);
}
</style>
