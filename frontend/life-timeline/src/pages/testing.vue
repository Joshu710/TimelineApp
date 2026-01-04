<script lang="ts" setup>
import { ref } from "vue";

// Variables for inputs
const event_name = ref("");
const event_desc = ref("");
const event_date = ref(new Date().toISOString().split("T")[0]);
const event_photos = ref([]);

// For checking if form is valid
const is_valid = ref(false);

// Rules to set Fields as required
const input_rules = [
  (value: any) => {
    if (value) return true;
    return "Field is Required";
  },
];

// Code to show preview of uploaded Images
const photo_urls = ref<string[]>([]);
function handlePreview() {
  console.log("previewing");
  photo_urls.value = [];
  if (event_photos.value) {
    for (let i = 0; i < event_photos.value.length; i++) {
      const photo: Blob | undefined = event_photos.value[i];
      if (photo) {
        console.log(event_photos.value[i]);
        photo_urls.value.push(URL.createObjectURL(photo));
      }
    }
  }
}

async function handleSubmit() {
  // If Form submition was valid
  if (!is_valid.value) {
    return;
  }

  //

  try {
    // Collecting Form data
    const form_data = new FormData();
    form_data.append("name", event_name.value);
    if (event_date.value) {
      const date = new Date(event_date.value).toISOString().split("T")[0];
      if (date) {
        form_data.append("date", date);
      }
    }
    form_data.append("desc", event_desc.value);
    if (event_photos.value) {
      for (let i = 0; i < event_photos.value.length; i++) {
        const photo: Blob | undefined = event_photos.value[i];
        if (photo) {
          form_data.append("photos[]", photo);
        }
      }
    }

    // Sending Form Data to the backend
    const response = await fetch("http://localhost:8000/api/add_event/", {
      method: "POST",
      body: form_data,
    });

    if (!response.ok) throw new Error("Network response was not ok");
    const data = await response.json();
    console.log(data);
  } catch (error) {
    console.error(error);
  }
}
</script>

<template>
  <!-- <HelloWorld /> -->
  <p>This is the testing page</p>

  <v-form v-model="is_valid" @submit.prevent="handleSubmit">
    <v-text-field
      :rules="input_rules"
      label="Event Name"
      v-model="event_name"
    ></v-text-field>
    <v-date-picker :rules="input_rules" v-model="event_date"></v-date-picker>
    <v-text-field
      :rules="input_rules"
      label="Description"
      v-model="event_desc"
    ></v-text-field>
    <v-file-input
      v-model="event_photos"
      accept="image/png, image/jpeg, image/bmp"
      label="Photos"
      placeholder="Upload your photos"
      prepend-icon="mdi-camera"
      multiple
      @change="handlePreview"
      @click:clear="handlePreview"
    ></v-file-input>
    <v-btn class="mt-2" type="submit" block>Submit</v-btn>
  </v-form>

  <div v-if="photo_urls">
    <p>Photo Preview</p>
    <v-img
      :width="100"
      :height="100"
      v-for="url in photo_urls"
      :src="url"
    ></v-img>
  </div>
</template>
