<template>
  <div class="twit-item"
    @click="favTwit(twit.id)">
    <div class="user-profile_twit">
        <div class="twit-item_user">
            @{{ username}}
        </div>
        <div class="twit-item_content">
            {{ twit.content }}
        </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'TwitItem',
  props: {
    //   used to pass data from parent to child
      username: {
          type: String,
          required: true
      },
      twit: {
          type: Object,
          required: true
      }
  },
  setup(props, context) {
      function favTwit(id) {
          // emit an event up the DOM tree
          context.emit('favourite', id)
      }

      return {
          favTwit
      }
  }
}
</script>

<style lang="scss" scoped>
/* styles only applicable to this component */
.twit-item {
    padding: 20px;
    background-color: white;
    border: 1px solid #dfe3e8;
    border-radius: 5px;
    box-sizing: border-box;
    cursor: pointer;
    transition: all 0.25s ease;
    width: 100%;
    margin-top: 5px;

    &.twit-item:hover {
        // & adds this styling to the parent
        transform: scale(1.1, 1.1)
    }

    .twit-item_user {
        font-weight: bold;
    }
}
</style>
