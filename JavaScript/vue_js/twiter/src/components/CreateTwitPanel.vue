<template>
    <form class="create-twit-panel"
        @submit.prevent="createNewTwit"
        :class="{ 'exceeded': newTwitCharCount > 180}">
        <label for="newTwit">
            <strong>Twit</strong>
            ({{ newTwitCharCount }}/180)
        </label>
        <textarea id="newTwit" rows="5"
            v-model="state.newTwitContent"/>

        <div class="create-twit-panel_submit">
            <div class="create-twit-type">
                <label for="newTwitType"><strong>Twit Type</strong></label>
                <select id="newTwitType"
                    v-model="state.selectedTwitType">
                    <option
                    :value="option.value"
                    v-for="(option, index) in state.twitTypes"
                    :key="index">
                        {{ option.name }}
                    </option>
                </select>
            </div>

            <button>Twit!</button>

        </div>
    </form>
</template>

<script>
// utilizes the Vue 3 composition API format
import { reactive, computed } from 'vue'

export default {
  name: 'CreateTwitPanel',
  setup(props, context) {
    //   sets up the component desired state in a state object
    const state = reactive({
        newTwitContent: '',
        selectedTwitType: 'instant',
        twitTypes: [
            { value: 'draft', name: 'Draft twit'},
            { value: 'instant', name: 'Instant twit'}
        ],
    })

    const newTwitCharCount = computed( () => state.newTwitContent.length)

    function createNewTwit() {
      if (state.newTwitContent && state.selectedTwitType !=='draft') {
        context.emit('add-twit', state.newTwitContent)
        state.newTwitContent = ''
      }
    }

    return {
        // return all component objects declared
        state,
        newTwitCharCount,
        createNewTwit
    }
  }
}
</script>

<style lang="scss" scoped>
.create-twit-panel {
    margin-top: 20px;
    padding: 20px 0;
    display: flex;
    flex-direction: column;

    textarea {
        border: 1px solid #dfe3e8;
        border-radius: 5px;
    }

    .create-twit-panel_submit {
        display: flex;
        justify-content: space-between;

        .create-twit-type {
            padding: 10px 0;
        }

        button {
            padding: 5px 20px;
            margin: auto 0;
            border-radius: 5px;
            border: none;
            background-color: deeppink;
            color: white;
            font-weight: bold;
        }
    }

    &.exceeded {
        color: red;
        border-color: red;

        .create-twit-panel_submit {
            button {
                background-color: red;
                color: white;
            }
        }
    }
}
</style>
