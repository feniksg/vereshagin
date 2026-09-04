<template>
  <canvas ref="canvasRef" class="connection-layer"></canvas>
</template>

<script setup>
import { ref, onMounted, onBeforeUnmount, nextTick, watch } from 'vue'

const props = defineProps({
  connections: {
    type: Array,
    required: true
  }
})

const canvasRef = ref(null)

function getCenterCoords(personId) {
  const el = document.querySelector(`[data-person-id="${personId}"]`)
  if (!el) return null
  const rect = el.getBoundingClientRect()
  const parentRect = canvasRef.value.parentNode.getBoundingClientRect()
  return {
    x: rect.left + rect.width / 2 - parentRect.left,
    y: rect.top + rect.height / 2 - parentRect.top
  }
}

function drawAllLines() {
  const canvas = canvasRef.value
  if (!canvas) return
  const ctx = canvas.getContext('2d')
  if (!ctx) return

  ctx.clearRect(0, 0, canvas.width, canvas.height)

  function drawCurvedLine(fromId, toId) {
    const c1 = getCenterCoords(fromId)
    const c2 = getCenterCoords(toId)
    if (!c1 || !c2) return

    ctx.beginPath()
    ctx.moveTo(c1.x, c1.y)
    const midX = (c1.x + c2.x) / 2
    const midY = (c1.y + c2.y) / 2 - 50
    ctx.quadraticCurveTo(midX, midY, c2.x, c2.y)
    ctx.strokeStyle = '#777'
    ctx.lineWidth = 3
    ctx.stroke()
  }

  props.connections.forEach(conn => {
    drawCurvedLine(conn.from, conn.to)
  })
}

function resizeCanvas() {
  const canvas = canvasRef.value
  if (!canvas) return
  const parentRect = canvas.parentNode.getBoundingClientRect()
  canvas.width = parentRect.width
  canvas.height = parentRect.height
  drawAllLines()
}

onMounted(() => {
  nextTick(() => {
    resizeCanvas()
  })
  window.addEventListener('resize', resizeCanvas)
})

onBeforeUnmount(() => {
  window.removeEventListener('resize', resizeCanvas)
})

watch(
  () => props.connections,
  () => {
    nextTick(() => {
      drawAllLines()
    })
  },
  { deep: true }
)
</script>

<style scoped>
.connection-layer {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  z-index: 0;      /* Линии под карточками */
  pointer-events: none;
}
</style>
