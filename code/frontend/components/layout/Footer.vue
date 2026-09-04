<template>
    <div class="footer">
            <div class="footer-hr"></div>
            <div class="footer-content">
                <div class="footer-item">
                    <h2>Основное</h2>
                    <ul>
                        <li><a href="biography">Биография</a></li>
                        <li><p>Семейное древо</p></li>
                        <li><p>Живопись</p></li>
                        <li><p>Графика</p></li>
                        <li><p>Книги</p></li>
                    </ul>
                </div>
                <div class="footer-item">
                    <h2>Архив</h2>
                    <ul>
                        <li><a href="ImageArchive">Архив изображений</a></li>
                        <li><a href="textArchive">Архив текстов</a></li>
                    </ul>
                </div>
                <div class="footer-item">
                    <h2>Медиа</h2>
                    <ul>
                        <li class="link"><NuxtLink to="https://www.xn--e1aogg7a.xn--p1ai/"><h2>Череповецкое<br> музейное  объединение</h2></NuxtLink></li>
                        <li class="link"><NuxtLink to="https://www.chsu.ru/"><h2>Череповецкий<br> государственный университет</h2></NuxtLink></li>
                    </ul>
                </div>
                <div class="footer-logo">
                    <NuxtLink to="/" class="logo">
                        <img src="@/assets/img/landing/img/logo.png" alt="logo"/>
                    </NuxtLink>
                </div>
            </div>
        </div>
</template>

<style lang="scss">
    .link {
        text-decoration: underline;
    }
    .logo {
        img {
            box-sizing:unset;
        }
    }
    a {
        text-decoration: none;
        color: inherit;
        &:hover {
            color: var(--color-primary);
            text-decoration: none;
        }
    }
    .footer{
        height: 100%;
        width: 100%;
        display: flex;
        justify-content: center;
        align-items: center;
        background-color: var(--color-background);
        min-height: 10vh;
        flex-direction: column;
        margin-top: 100px;
    }
    .footer-hr {
        width: 78.19%;
        height: 0px;
        border: 1px solid var(--color-primary);
        margin: 20px 0;
        max-width: 1440px;
    }
    .footer-content {
        display: flex;
        flex-direction: row;
        width: 78.19%;
        padding: 25px 50px;
        max-width: 1440px;
    }
    .footer-item li {
        font-size: 14px;
        font-weight: 400;
        line-height: 17px;
    }
    
    .footer-item ul {
        list-style-type: none;
        padding: 0px;
    }
    .footer-item li {
        margin: 0px;
        margin-bottom: 25px;
    }
    .footer-item li > h2{
        
    }
    .footer-item{
        /* flex: 2; */
        max-width: 15%;
        margin-right: 80px;
    }
    .footer-logo {
        /* flex: 4; */
        display: flex;
        flex-direction: row-reverse;
        margin-left: auto;
    }
</style>