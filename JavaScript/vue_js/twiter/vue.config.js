module.exports = {
  // vue app launch conifgs (not hot reloaded, need app restart)
    css: {
      loaderOptions: {
        sass: {
          additionalData: '@import "@/styles/base.scss";'
        }
      }
    }
}
