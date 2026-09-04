<template>
  <div class="auth-container">
    <div class="auth-card">
      <h1 class="text-center">{{ isLogin ? 'Вход' : 'Регистрация' }}</h1>
      <form @submit.prevent="handleSubmit" class="auth-form">
        <div v-if="!isLogin">
          <label>ФИО</label>
          <input v-model="registerForm.fullName" type="text" required />

          <label>Статус</label>
          <select v-model="registerForm.status" required>
            <option disabled value="">Выберите статус</option>
            <option>Школьник</option>
            <option>Студент</option>
            <option>Преподаватель</option>
            <option>Научный исследователь</option>
          </select>

          <label>Место учёбы/работы</label>
          <input v-model="registerForm.place" type="text" required />
        </div>

        <!-- email -->
            <label>Электронная почта</label>
            <input
            :value="isLogin ? loginForm.email : registerForm.email"
            @input="(e) => isLogin ? loginForm.email = e.target.value : registerForm.email = e.target.value"
            type="email"
            required
            />

            <!-- password -->
            <label>Пароль</label>
            <input
            :value="isLogin ? loginForm.password : registerForm.password"
            @input="(e) => isLogin ? loginForm.password = e.target.value : registerForm.password = e.target.value"
            type="password"
            required
            />
        <div v-if="!isLogin">
          <label>Подтверждение пароля</label>
          <input v-model="registerForm.confirmPassword" type="password" required />
        </div>

        <button type="submit">
          {{ isLogin ? 'Войти' : 'Зарегистрироваться' }}
        </button>
      </form>

      <p class="switch-link text-center">
        {{ isLogin ? 'Нет аккаунта?' : 'Уже есть аккаунт?' }}
        <a href="#" @click.prevent="toggleForm">
          {{ isLogin ? 'Зарегистрироваться' : 'Войти' }}
        </a>
      </p>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRoute } from 'vue-router'
const route = useRoute()

onMounted(() => {
  if (route.query.mode === 'register') {
    isLogin.value = false
  } else {
    isLogin.value = true
  }
})


const isLogin = ref(true)
const API_URL = 'http://localhost:8000'


const loginForm = ref({
  email: '',
  password: ''
})

const registerForm = ref({
  fullName: '',
  status: '',
  place: '',
  email: '',
  password: '',
  confirmPassword: ''
})

const toggleForm = () => {
  isLogin.value = !isLogin.value
}

const register = async () => {
  if (registerForm.value.password !== registerForm.value.confirmPassword) {
    alert('Пароли не совпадают')
    return
  }

  try {
    await $fetch(`${API_URL}/users/register`, {
      method: 'POST',
      body: {
        full_name: registerForm.value.fullName,
        status: registerForm.value.status,
        place: registerForm.value.place,
        email: registerForm.value.email,
        password: registerForm.value.password
      }
    })
    alert('Регистрация прошла успешно')
    isLogin.value = true
  } catch (e) {
    console.error(e)
    alert('Ошибка регистрации: ' + (e?.data?.detail || e.message))
  }
}

const login = async () => {
  try {
    const data = await $fetch(`${API_URL}/users/login`, {
      method: 'POST',
      body: {
        email: loginForm.value.email,
        password: loginForm.value.password
      }
    })
    localStorage.setItem('token', data.token || '') // если вы позже добавите токен
    isLogin.value = true
    navigateTo('/')
    alert('Успешный вход')
    navigateTo('/dashboard')
  } catch (e) {
    if (e.data?.detail) {
      alert('Ошибка входа: ' + e.data.detail)
    } else {
      console.error(e)
      alert('Ошибка входа: ' + JSON.stringify(e))
    }
  }
}


const handleSubmit = () => {
  isLogin.value ? login() : register()
}

const logout = () => {
  localStorage.removeItem('token')
  navigateTo('/')
}
</script>


<style scoped>
.auth-container {
  min-height: 100vh;
  width: auto;
  display: flex;
  justify-content: center;
  align-items: center;
  background: #f5f5f5;
  padding: 20px;
}

.auth-card {
  background: white;
  border: 1px solid #111;
  border-radius: 10px;
  padding: 30px 40px;
  width: 100%;
  max-width: 400px;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
  text-align: left;
}

.auth-form {
  display: flex;
  flex-direction: column;
}

.auth-form label {
  margin-top: 10px;
  font-weight: bold;
}

.auth-form input,
.auth-form select {
  margin-top: 5px;
  padding: 8px;
  font-size: 14px;
  border-radius: 4px;
  border: 1px solid #ccc;
}

.auth-form button {
  margin-top: 20px;
  padding: 10px;
  background: #111;
  color: white;
  border: none;
  border-radius: 6px;
  cursor: pointer;
  font-size: 16px;
}

.auth-form button:hover {
  background: #333;
}

.switch-link {
  margin-top: 15px;
  font-size: 14px;
}

.switch-link a {
  color: #0070f3;
  text-decoration: underline;
  cursor: pointer;
}
</style>
