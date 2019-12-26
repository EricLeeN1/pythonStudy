module.exports = {
    title: "pythonStudy 文档",
    description: "python study",
    base: '/',
    themeConfig: {
        nav: [{
            text: "基础文档",
            link: 'base'
        }, {
            text: "基础文档",
            link: 'base'
        }, {
            text: "基础文档",
            link: 'base'
        }]
    },
    sidebar: {
        '/': [
            "/", //指的是根目录的md文件 也就是 README.md 里面的内容
            "apiword", //根目录创建 apiword.md文件 
            "api", //根目录创建 api.md文件 
            "error" //根目录创建 error.md文件
        ]
    },
    sidebarDepth: 2
}