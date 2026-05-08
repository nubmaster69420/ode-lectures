photo_2026-05-01 12.40.36 PM.jpeg -- 0

 --- 

# 04.09.25 Лекция. Глава 1: Задача Коши для дифференциальных уравнений

## §1 Разрешимость задачи Коши

$<a, b> : (a, b); [a, b]; (a, b]; [a, b)$

$C(D)$ — множество непрерывных на $D$ функций, т.е. $y(t) \in C(D)$ означает, что $y(t)$ непрерывна на $D$.

$C^k(D)$ — множество $k$ раз непрерывно дифференцируемых функций.

$$f(t,y) = \begin{pmatrix} f_1(t,y) \\ \vdots \\ f_n(t,y) \end{pmatrix} \quad f(t,y) \in C(D) \iff \forall i=1, \dots, n \quad f_i(t,y) \in C(D)$$

Дифференциальное уравнение $\hat{F}(t, y(t), y'(t)) = 0$

$y' = f(t, y) \quad (1)$

$G \subseteq \mathbb{R}^{n+1}$ — область ($G$ — линейно связное и открытое)

$f: G \to \mathbb{R}^n$

- $t$ — независимая переменная
- $y$ — неизвестная функция (решение)

$$f(t,y) = \begin{pmatrix} f_1(t,y) \\ \vdots \\ f_n(t,y) \end{pmatrix}, \quad f_i(t,y) = f_i(t, y_1, \dots, y_n) \in C(G)$$

### Опр.
Функция $y(t)$, определенная на $<a, b>$, называется решением (1), если:
1) $y(t) \in C^1(<a, b>)$
2) $(t, y(t)) \in G$ при $t \in <a, b>$
3) $\frac{dy}{dt}(t) = f(t, y(t))$ при $t \in <a, b>$

### Пример
1) $y' = y^2$
- $y_1(t) = -\frac{1}{t}, t \in \mathbb{R} \setminus \{0\}$ — не решение (не связное множество)
- $y_{2,3}(t) = -\frac{1}{t}, t \in (0, \infty) \cup (-\infty, 0)$ — решения (два на каждом из интервалов)
- $y_4(t) = -\frac{1}{t}, t \in (0, 1)$ — решение (продолжаемое)
- $y_5(t) = 0, t \in \mathbb{R}$ — решение

### Опр.
Пусть $y(t)$ определена на $<a, b>$, является решением (1), тогда $(t, y(t))$ при $t \in <a, b>$ называется интегральной кривой (1).
{Интегральная кривая — график решения (1)}

 --- 

photo_2026-05-01 12.40.38 PM.jpeg -- 1

 --- 

# Задача Коши. Теоремы существования и единственности

### Опр.
Задача о нахождении решения (1), принимающего значение $y_0$ в точке $t_0$, называется **задачей Коши (ЗК)**.

$$
\begin{cases}
\frac{dy}{dt} = f(t, y) \\
y(t_0) = y_0
\end{cases} \quad (2)
$$

$(t_0, y_0)$ — начальные данные.

**Геометрическая интерпретация:** Задача Коши — задача о нахождении интегральной кривой, проходящей через $(t_0, y_0)$.

[ГРАФИК: Оси $t$ и $y$, кривая проходит через $(t_0, y_0)$, касательная имеет угол $\alpha$, где $\operatorname{tg} \alpha = f(t_0, y_0)$]

Введём цилиндрическую область $Ц = \{ (t, y) \in \mathbb{R}^{n+1} \mid |t - t_0| < T, \|y - y_0\| < \rho \}$.

### Теорема Пеано
Пусть $\bar{Ц}$ (замыкание $Ц$) $\subseteq G$ и $f(t, y) \in C(\bar{Ц}) \Rightarrow \exists$ решение ЗК (2), определённое при $|t - t_0| \le T_0$, где $T_0 = \min \{ T, \frac{\rho}{F} \}$, $F = \max_{(t, y) \in \bar{Ц}} \|f(t, y)\|$.

### Пример
1) $$ \begin{cases} \frac{dy}{dt} = 3 y^{\frac{2}{3}} \\ y(0) = 0 \end{cases} $$

---
**\*** Условие Липшица:
$$ \exists L > 0 \mid \forall (t, y^1), (t, y^2) \in \bar{Ц} : \|f(t, y^1) - f(t, y^2)\| \le L \|y^1 - y^2\| $$
---

### Теорема Пикара
Пусть $\bar{Ц} \subseteq G$ и выполнены следующие условия:
1. $f(t, y) \in C(\bar{Ц})$
2. $f(t, y)$ удовлетворяет условию Липшица (липшицевость) по аргументу $y$ в $\bar{Ц}$.

Тогда $\exists!$ решение ЗК (2), определённое при $|t - t_0| \le T_0$, где $T_0 = \min \{ T, \frac{\rho}{F} \}$, $F = \max_{(t, y) \in \bar{Ц}} \|f(t, y)\|$.

### Доказательство
В док-ве будет 4 шага:
- 1-й шаг: сведение задачи Коши к интегральному уравнению.
- 2-й шаг: метод последовательных (Пикаровских) приближений.
- 3-й шаг: равномерная сходимость.
- 4-й шаг: единственность.

Для доказательства [НРЗБ: вспомним сведения из] мат. анализа.

### Опр.
$a_k(t)$ — последовательность функций на $\langle a, b \rangle$. Она сходится поточечно к функции $A(t)$, если $\forall t \in \langle a, b \rangle \ \forall \varepsilon > 0 \ \exists K_0 \in \mathbb{N} \dots$

### Опр.
Говорят, что $a_k(t)$ сходится равномерно к $A(t)$, если $\forall \varepsilon > 0 \ \exists K_0 \in \mathbb{N} \dots$
$$ \sum_{k=0}^\infty b_k(t) $$

### Опр.
Ряд $\sum_{k=0}^\infty b_k(t)$ сходится равномерно к $S(t)$, если $S_k = \sum_{j=0}^k b_j(t)$ сходится равномерно к $S(t)$.

### Тм (о равномерной сходимости)
Пусть:
1. $b_k(t) \in C[a, b]$
2. $\sum_{k=0}^\infty b_k(t)$ сходится равномерно.

Тогда ряд $\sum_{k=0}^\infty b_k(t)$ [НРЗБ: представляет собой непрерывную функцию].

### Тм (признак Вейерштрасса)
Пусть:
1. $|b_k(t)| \le c_k$
2. ряд $\sum c_k$ сходится.

Тогда ряд $\sum b_k(t)$ сходится абсолютно и равномерно.

**Непосредственно доказательство:**
**1-й шаг:** Пусть $y(t)$ — [НРЗБ: решение] ЗК (2), удовлетворяет условиям:
1. $y(t) \in C^1(|t - t_0| \le T_0)$

 --- 

photo_2026-05-01 12.40.40 PM.jpeg -- 2

 --- 

# Доказательство теоремы (3-й и 4-й шаги)

3-й шаг: равномерно сходящаяся последовательность
4-й шаг: единственность

Для доказательства этой Тм понадобится некоторая прелюдия на мат. анализе.

### Опр.
$a_k(t)$ — последовательность функций. Говорят, что $a_k(t)$ сходится поточечно к функции $a(t)$ ($a_k(t) \to a(t)$) на $\langle a, b \rangle$, если
$$ \forall t \in \langle a, b \rangle \quad \forall \varepsilon > 0 \quad \exists k_0 \quad \forall k > k_0 \quad \| a_k(t) - a(t) \| < \varepsilon $$

### Опр.
Говорят, что $a_k(t)$ сходится равномерно на $\langle a, b \rangle$ ($a_k(t) \rightrightarrows a(t)$), если
$$ \forall \varepsilon > 0 \quad \exists k_0 \in \mathbb{N} \mid \forall t \in \langle a, b \rangle \quad \forall k > k_0 \quad \| a_k(t) - a(t) \| < \varepsilon $$

$$ \sum_{k=0}^{\infty} b_k(t) $$

### Опр.
Ряд $\sum_{k=0}^{\infty} b_k(t)$ сходится равномерно на $\langle a, b \rangle$, если последовательность $s_n = \sum_{k=0}^n b_k(t)$ сходится равномерно на $\langle a, b \rangle$.

### Тм (о равномерной сходимости ряда непрерывных функций)
Пусть:
- 1) $b_k(t) \in C(\langle a, b \rangle)$
- 2) $\sum_{k=0}^{\infty} b_k(t)$ сходится равномерно на $\langle a, b \rangle$

Тогда ряд $\sum_{k=0}^{\infty} b_k(t)$ [НРЗБ: р-но сходится] на $\langle a, b \rangle$.

### Тм (признак Вейерштрасса о равномерной сходимости)
Пусть:
- 1) $| b_k(t) | \le C_k, \quad k = 0, 1, \dots$
- 2) ряд $\sum_{k=0}^{\infty} C_k$ сходится \hfill (конец прелюдии...)

Тогда ряд $\sum_{k=0}^{\infty} b_k(t)$ равномерно сходится на $\langle a, b \rangle$.

### Непосредственно доказательство П:
#### 1-й шаг
Пусть $y(t)$ — решение (2), определённое при $| t - t_0 | \le T_0$, тогда $y(t)$ удовлетворяет условиям:
- 1) $y(t) \in C^1(| t - t_0 | \le T_0)$

 --- 

photo_2026-05-01 12.40.42 PM.jpeg -- 3

 --- 

# Лекция (11.09.23)

- 2) $(t, y(t)) \in G$ при $|t - t_0| \le T_0$
- 3) $\frac{dy}{dt}(t) = f(t, y(t))$ при $|t - t_0| \le T_0$ 
- 4) $y(t_0) = y_0$

Проинтегрируем 3) от $t_0$ до $t$:
$$y(t) - y(t_0) = \int_{t_0}^t f(s, y(s)) \, ds$$
$$y(t) = y_0 + \int_{t_0}^t f(s, y(s)) \, ds \Rightarrow y(t) \text{ — решение (3) определённое при } |t - t_0| \le T_0$$

Получим следующие, изменённые условия:
- $1') y(t) \in C(|t - t_0| \le T_0)$
- $2') (t, y(t)) \in G \text{ при } |t - t_0| \le T_0$
- $3') y(t) \equiv y_0 + \int_{t_0}^t f(s, y(s)) \, ds \text{ при } |t - t_0| \le T_0$

Покажем, что если $y(t)$ — решение (3), определённое при $|t - t_0| \le T_0$, то $y(t)$ — решение ЗК (2), определённое при $|t - t_0| \le T_0$
- $2) \sim 2')$
- 4) вытекает из $3')$ при $t = t_0$
- Из $1') y(t) \in C(|t - t_0| \le T_0) \Rightarrow f(t, y(t)) \in C(|t - t_0| \le T_0) \Rightarrow$
$\Rightarrow \int_{t_0}^t f(s, y(s)) \, ds \in C^1(|t - t_0| \le T_0) \Rightarrow y(t) \in C^1(|t - t_0| \le T_0)$
получим $1) \sim 1')$
дифференцируя получим 3) из $3')$

### 2-й шаг:
Рассмотрим последовательность:
$$
\begin{cases}
y^{[0]}(t) = y_0 \\
y^{[k+1]}(t) = y_0 + \int_{t_0}^t f(s, y^{[k]}(s)) \, ds 
\end{cases}
$$
(Пикаровские приближения)

Покажем, что последовательность определена корректно, т.е. $(t, y^{[k]}(t)) \in \bar{G}$ при $|t - t_0| \le T_0$, $k = 0, 1, \dots$ эквивалентно $\| y^{[k]}(t) - y_0 \| \le \rho$.

Тут ведём рассуждения по индукции:
При $k = 0$:
$\| y^{[0]}(t) - y_0 \| = 0 \le \rho$

Предположим $\| y^{[k]}(t) - y_0 \| \le \rho$

### 3-й шаг:
Равномерная сходимость
$\| y^{[1]}(t) - y^{[0]}(t) \| = \| \int_{t_0}^t f(s, y^{[0]}(s)) \, ds \| \le \int_{t_0}^t \| f(s, y_0) \| \, ds$

$\| y^{[2]}(t) - y^{[1]}(t) \| \le \int_{t_0}^t \| f(s, y^{[1]}(s)) - f(s, y^{[0]}(s)) \| \, ds \le L \int_{t_0}^t \| y^{[1]}(s) - y^{[0]}(s) \| \, ds$

Можно показать [НРЗБ].
Тогда оценки:
$\| y^{[0]}(t) \| \le \| y_0 \|$
$\| y^{[1]}(t) \| \le \| y_0 \| + [НРЗБ]$
Тогда по [НРЗБ] сходится равномерно $\Rightarrow \lim_{k \to \infty} y^{[k+1]}(t) = y(t)$
$y(t) = y_0 + \int_{t_0}^t f(s, y(s)) \, ds$

### 4-й шаг:
Предположим [НРЗБ]

 --- 

photo_2026-05-01 12.40.44 PM.jpeg -- 4

 --- 

# Доказательство теоремы существования и единственности решения задачи Коши (продолжение)

Предположим, что $\| y^{[k-1]}(t) - y_0 \| \le \rho$ при $|t - t_0| \le T_0$, тогда
$$ \| y^{[k]}(t) - y_0 \| = \left\| \int_{t_0}^t f(s, y^{[k-1]}(s)) \, ds \right\| \le \left| \int_{t_0}^t \| f(s, y^{[k-1]}(s)) \| \, ds \right| \le F |t - t_0| \le F T_0 \le \rho $$
$$ T_0 = \min \left\{ T, \frac{\rho}{F} \right\} $$

### 3-й шаг
$$ y^{[k]}(t) = y^{[k-1]}(t) + y^{[k]}(t) - y^{[k-1]}(t) = \dots = y^{[0]}(t) + \sum_{j=0}^{k-1} (y^{[j+1]}(t) - y^{[j]}(t)) \quad \boxtimes $$

Равномерная сходимость $\sum_{j=0}^{\infty} (y^{[j+1]}(t) - y^{[j]}(t))$ эквивалентна равномерной сходимости $y^{[k]}(t)$ при $|t - t_0| \le T_0$.
$$ \| y^{[1]}(t) - y^{[0]}(t) \| = \left\| \int_{t_0}^t f(s, y^{[0]}(s)) \, ds \right\| \le F |t - t_0| $$
$$ \| y^{[2]}(t) - y^{[1]}(t) \| = \left\| \int_{t_0}^t (f(s, y^{[1]}(s)) - f(s, y^{[0]}(s))) \, ds \right\| \le $$
$$ \le \left| \int_{t_0}^t \| f(s, y^{[1]}(s)) - f(s, y^{[0]}(s)) \| \, ds \right| \le F L \left| \int_{t_0}^t |s - t_0| \, ds \right| = F L \frac{|t - t_0|^2}{2} $$

Можно показать по индукции, что $\| y^{[k]}(t) - y^{[k-1]}(t) \| \le F L^{k-1} \frac{|t - t_0|^k}{k!}$.

Тогда оценим $\boxtimes$ (перейдем к $\infty$ дабы использовать прогрессию):
$$ \left\| y^{[0]}(t) + \sum_{j=0}^{\infty} (y^{[j+1]}(t) - y^{[j]}(t)) \right\| \le \| y^{[0]}(t) \| + \sum_{j=0}^{\infty} \| y^{[j+1]}(t) - y^{[j]}(t) \| \le $$
$$ \le \| y_0 \| + \sum_{j=0}^{\infty} F L^j \frac{|t - t_0|^{j+1}}{(j+1)!} = \| y_0 \| + \frac{F}{L} \sum_{i=1}^{\infty} \frac{(L |t - t_0|)^i}{i!} = \| y_0 \| + \frac{F}{L} \left( e^{L |t - t_0|} - 1 \right) \le $$
$$ \le \| y_0 \| + \frac{F}{L} \left( e^{L T_0} - 1 \right) $$

Тогда по признаку Вейерштрасса о равномерной сходимости, последовательность $y^{[k]}(t)$ сходится равномерно при $|t - t_0| \le T_0$
$$ \Rightarrow \lim_{k \to \infty} y^{[k]}(t) = y(t) \in C(|t - t_0| \le T_0) $$

$$ y^{[k+1]}(t) = y_0 + \int_{t_0}^t f(s, y^{[k]}(s)) \, ds $$
$$ \downarrow k \to \infty $$
$$ y(t) = y_0 + \int_{t_0}^t f(s, y(s)) \, ds \Rightarrow y(t) = \lim_{k \to \infty} y^{[k]}(t) \text{ — решение задачи Коши} $$

### 4-й шаг
Предположим, что $y^1(t), y^2(t)$ — решение задачи Коши при $|t - t_0| \le T_0$

 --- 

photo_2026-05-01 12.40.46 PM.jpeg -- 5

 --- 

# Единственность решения задачи Коши

### Доказательство (продолжение)

Пусть $y^1(t) \not\equiv y^2(t)$. Тогда согласно шагу 1 имеем:
$$y^1(t) = y_0 + \int_{t_0}^t f(s, y^1(s)) \, ds$$
$$y^2(t) = y_0 + \int_{t_0}^t f(s, y^2(s)) \, ds$$
$$\|y^2(t) - y^1(t)\| = \left\| \int_{t_0}^t (f(s, y^2(s)) - f(s, y^1(s))) \, ds \right\| \le \int_{t_0}^t \|f(s, y^2(s)) - f(s, y^1(s))\| \, ds \le$$
$$\le L \int_{t_0}^t \|y^2(s) - y^1(s)\| \, ds$$
$$\|y^2(t) - y^1(t)\| \le L \underbrace{\int_{t_0}^t \|y^2(s) - y^1(s)\| \, ds}_{\sigma(t) \ge 0}$$
$$\frac{d}{dt} \sigma(t) = \|y^2(t) - y^1(t)\| \le L \sigma(t)$$
$$\frac{d}{dt} \sigma(t) - L \sigma(t) \le 0 \quad \left| \cdot e^{-Lt} \right.$$
$$e^{-Lt} \frac{d}{dt} \sigma(t) + \left( \frac{d}{dt} e^{-Lt} \right) \sigma(t) \le 0$$
$$\frac{d}{dt} (e^{-Lt} \sigma(t)) \le 0 \quad \left| \int_{t_0}^t \right.$$
$$\sigma(t) \le \sigma(t_0) = 0 \Rightarrow \sigma(t) \equiv 0 \Rightarrow y^1(t) \equiv y^2(t) \text{ противоречие } \blacksquare$$

### Замечание
Пусть $y(t)$ — решение задачи Коши, $y^{[k]}(t)$ — пикаровские приближения $\Rightarrow \|y(t) - y^{[k]}(t)\| \le F L^{k-1} \cdot \frac{|t - t_0|^k}{k!}$ при $|t - t_0| \le T_0$

### Th Осгуда
Пусть справедлива оценка $\|f(t, y^2) - f(t, y^1)\| \le \varphi(\|y^2 - y^1\|)$
$0 < \varphi(y)$ при $y \in (0, y^*)$ при этом $\int_{\epsilon}^{y^*} \frac{1}{\varphi(z)} dz \xrightarrow[\epsilon \to 0]{} \infty \Rightarrow$
$\Rightarrow$ через каждую точку $(t_0, y_0) \in G$ проходит не более 1-й интегральной кривой.

 --- 

photo_2026-05-01 12.40.47 PM.jpeg -- 6

 --- 

# 18.09.25 лекция

### Th (Осгуда)
$$\|f(t, y') - f(t, y'')\| \leq \varphi(\|y' - y''\|) \quad \varphi(\eta) > 0 \quad u_0 \geq \eta > 0$$
$$\int_{\varepsilon}^{u_0} \frac{1}{\varphi(\eta)} d\eta \xrightarrow[\varepsilon \to 0]{} \infty \Rightarrow \exists ! \text{ реш. ЗК}$$
$$\varphi_1(\eta) = k|\eta| \quad \varphi_2(\eta) = k|\eta| \ln |\eta|$$

## § 2 Линейные системы диф-х уравнений
$$\frac{dy}{dt} = A(t)y + h(t)$$
$$A(t) \in M_{n \times n}(\mathbb{R})$$
$$A(t) \in C(t_1, t_2) \quad (t_1, t_2) \subseteq \mathbb{R}$$
$$h(t) \in C(t_1, t_2)$$

$$
(2) \begin{cases} 
\frac{d}{dt} y = A(t)y + h(t) \\ 
y(t_0) = y^0 
\end{cases} 
\quad y^0 \in \mathbb{R}^n, \quad \forall t_0 \in (t_1, t_2) \text{ фикс}
$$

### Th №1 (Пикар) для лин. систем
$$\forall t_0 \in (t_1, t_2) \quad \forall y^0 \in \mathbb{R}^n \quad \forall h(t) \in C(t_1, t_2) \quad \exists ! \text{ реш. (2)} \quad y(t) \in C^1(t_1, t_2)$$

### Доказательство (эквивалентность)
Теперь аналогом уравнения (2) будет 
$$y(t) = y^0 + \int_{t_0}^t (A(s)y(s) + h(s)) ds \quad (3)$$
Аналогично строим последовательность:
- $y^{[0]}(t) = y^0$
- $y^{[j+1]}(t) = y^0 + \int_{t_0}^t (A(s)y^{[j]}(s) + h(s)) ds$

В силу того всё определено на $(t_1, t_2)$, то каждый элемент последовательности будет на $(t_1, t_2)$ определён.

### Замечание
С учётом $*$ задача (2) выглядит:
$$
\begin{cases} 
\frac{d}{dt} y_1 = a_{11}(t)y_1 + \dots + a_{1n}(t)y_n + h_1(t) \\ 
\dots \\ 
\frac{d}{dt} y_n = a_{n1}(t)y_1 + \dots + a_{nn}(t)y_n + h_n(t) 
\end{cases}
$$
$$
\begin{cases}
y_1(t_0) = y_1^0 \\
\dots \\
y_n(t_0) = y_n^0
\end{cases}
$$

$*$:
$$A(t) = \begin{pmatrix} a_{11}(t) & a_{12}(t) & \dots & a_{1n}(t) \\ \dots & \dots & \dots & \dots \\ a_{n1}(t) & a_{n2}(t) & \dots & a_{nn}(t) \end{pmatrix}$$
$$h(t) = \begin{pmatrix} h_1(t) \\ \dots \\ h_n(t) \end{pmatrix} \quad y(t) = \begin{pmatrix} y_1(t) \\ \dots \\ y_n(t) \end{pmatrix} \quad y^0 = \begin{pmatrix} y_1^0 \\ \dots \\ y_n^0 \end{pmatrix}$$

### Замечание (про липшицевость)
$\forall [\tilde{t}_1, \tilde{t}_2] \subset (t_1, t_2)$
$t_0 \in [\tilde{t}_1, \tilde{t}_2]$
$$\|f(t, y') - f(t, y'')\| \leq L \|y' - y''\|$$

 --- 

photo_2026-05-01 12.40.49 PM.jpeg -- 7

 --- 

$$ \| (A(t)y' + h(t)) - (A(t)y'' + h(t)) \| = \| A(t)(y' - y'') \| \le \| A(t) \| \cdot \| y' - y'' \| $$
т.е. имеем липшицевость; выбираем $\max_{t \in [T_1, T_2]} \| A(t) \|$

Тогда $y^{(k)}(t) \rightrightarrows y(t)$ на $[T_1, T_2]$. Единственность из Тн. Пикара. $\blacksquare$

### Следствие
Пусть $A(t) \equiv A, h(t) \equiv 0 \implies \forall t_0 \in \mathbb{R}, \forall y^0 \in \mathbb{R}^n \exists!$ решение ЗК (2)
*Пикаровские приближения, начиная с нуля:*
$$ y(t) = \left[ \sum_{j=0}^{\infty} \frac{(t-t_0)^j}{j!} A^j \right] y^0 $$
**матричная экспонента**

### Следствие
Пусть $A(t) \equiv A, h(t) \in C(\mathbb{R})$, тогда $\forall t_0 \in \mathbb{R} \ \forall y^0 \in \mathbb{R}^n \exists!$ решение
$$ \begin{cases} \frac{dy}{dt} = Ay + h(t) \\ y(t_0) = y_0 \end{cases} $$
и
$$ y(t) = e^{(t-t_0)A} y^0 + \int_{t_0}^t e^{(t-s)A} h(s) \, ds $$
**формула Коши**

# 25.09.23 лекция

$$ (2) \begin{cases} \frac{dy}{dt} = A(t)y + h(t) \\ y(t_0) = y^0 \end{cases} $$
*Теперь посмотрим на всё это без требования вещественнозначности*

- $A(t) = A^1(t) + i A^2(t); \ A^1(t), A^2(t)$ — веществ.
- $h(t) = h^1(t) + i h^2(t); \ h^1(t), h^2(t)$ — веществ.
- $y^0 = u^0 + i v^0, \ u^0, v^0$ — веществ.

### Th
$$ A(t) \in C(t_1, t_2) $$
$$ h(t) \in C(t_1, t_2) $$
$\implies \forall t_0 \in (t_1, t_2) \ \forall y^0 = u^0 + i v^0 \ \exists!$ реш. (2) $y(t) \in C^1(t_1, t_2)$.

### Доказательство
Предположим, что $\exists$ решение (2) $y(t) = u(t) + i v(t)$, тогда:
$$ \frac{d}{dt} y(t) = \frac{d}{dt} u(t) + i \frac{d}{dt} v(t) $$
$$ A(t)y(t) + h(t) \equiv (A^1(t) + i A^2(t))(u(t) + i v(t)) + h^1(t) + i h^2(t) $$

 --- 

photo_2026-05-01 12.40.50 PM.jpeg -- 8

 --- 

# Обыкновенные дифференциальные уравнения

Распишем тождества (тождества имеем ввиду следующего: комплекснозначные функции эквивалентны тогда и только тогда, когда $Re$ и $Im$ совпадают):

$$\frac{d u(t)}{dt} \equiv A^1(t)u(t) - A^2(t)v(t) + h^1(t)$$
$$\frac{d v(t)}{dt} \equiv A^1(t)v(t) + A^2(t)u(t) + h^2(t)$$

$$u(t_0) + i v(t_0) \equiv y^0 = u^0 + i v^0 \text{ из начальных условий}$$

$\begin{pmatrix} u(t) \\ v(t) \end{pmatrix}$ — реш. ЗК, восстановим исходя из этого систему:

$$(*) \begin{cases} \frac{d}{dt} \begin{pmatrix} u \\ v \end{pmatrix} = \begin{pmatrix} A^1(t) & -A^2(t) \\ A^2(t) & A^1(t) \end{pmatrix} \begin{pmatrix} u \\ v \end{pmatrix} + \begin{pmatrix} h^1(t) \\ h^2(t) \end{pmatrix} \\ \begin{pmatrix} u \\ v \end{pmatrix}(t_0) = \begin{pmatrix} u^0 \\ v^0 \end{pmatrix} \end{cases} \text{ — а для этого доказали ранее}$$

### Следствие
$A(t) \equiv A = \text{const } (n \times n) \quad A = A^1 + i A^2 \Rightarrow$

1) $h(t) \equiv 0$
$$y(t) = e^{(t-t_0)A} y^0$$

2) $h(t) \not\equiv 0$
$$y(t) = e^{(t-t_0)A} y^0 + \int_{t_0}^t e^{(t-s)A} h(s) ds$$

### Док-во п. (1)
Метод вариации произвольной постоянной будет использован в док-ве 2).
$$e^{sA} = E + \frac{s}{1!} A + \frac{s^2}{2!} A^2 + \dots \quad \forall s \in [t_1, t_2]$$

Поймем, что ряд сходится равномерно, (в каком-то смысле [НРЗБ: гармонически]):
$$\| e^{sA} \| = \| E + \frac{s}{1!} A + \frac{s^2}{2!} A^2 + \dots \| \le 1 + \frac{|s|}{1!} \|A\| + \frac{|s|^2}{2!} \|A\|^2 + \dots = e^{|s| \cdot \|A\|}$$

$$\frac{d}{ds} (e^{sA}) = A e^{sA} = e^{sA} A \quad (h \equiv 0)$$
$$y(t) = e^{tA} e^{-t_0 A} y^0$$
$$\frac{dy}{dt} = Ay$$
$$y(t) = e^{tA} C, \quad \forall C = \begin{pmatrix} c_1 \\ \vdots \\ c_n \end{pmatrix}$$

$$\frac{dy(t)}{dt} - Ay(t) = 0$$
$$e^{-tA} \frac{d}{dt} y(t) - A e^{-tA} y(t) \equiv 0 \quad (\text{используем } \frac{d}{dt} (e^{-tA}))$$
$$e^{-tA} \frac{d}{dt} y(t) + \frac{d}{dt} (e^{-tA}) y(t) = 0; \quad \frac{d}{dt} (e^{-tA} y(t)) = 0 \Rightarrow y(t) = e^{tA} C$$
тут можно подставить нач. условия и найти $C$.
$$y(t_0) = y_0$$

 --- 

photo_2026-05-01 12.40.51 PM.jpeg -- 9

 --- 

# Линейные неоднородные системы и сведение уравнения $n$-го порядка к системе

2) $h(t) \neq 0$

Тогда попробуем: $y(t) = e^{tA} c(t)$, тогда $c(t) = ?$

$$\frac{d}{dt} y(t) \equiv A e^{tA} c(t) + e^{tA} \frac{d}{dt} c(t)$$

$$A y(t) + h(t) = A e^{tA} c(t) + h(t)$$

Тогда приходим к следующему:

$$\begin{cases} e^{tA} \frac{d}{dt} c(t) \equiv h(t) \Rightarrow \frac{d}{dt} c(t) \equiv e^{-tA} h(t) \quad (*) \\ e^{t_0 A} c(t_0) = y^0 \sim c(t_0) = e^{-t_0 A} y^0 \end{cases}$$

$$(*) \int_{t_0}^t \frac{d}{ds} c(s) \, ds = \int_{t_0}^t e^{-sA} h(s) \, ds$$

$$c(t) - c(t_0)$$

Тогда $c(t) = e^{-t_0 A} y^0 + \int_{t_0}^t e^{-sA} h(s) \, ds$ ∎

$$u^{(n)} = g(t, u, u', \dots, u^{(n-1)})$$

$$g(t, y_1, \dots, y_n) \in C(G), \quad G \subset \mathbb{R}^{n+1}$$

$$y(t) = \begin{pmatrix} u(t) \\ \vdots \\ u^{(n-1)}(t) \end{pmatrix} = \begin{pmatrix} y_1(t) \\ \vdots \\ y_n(t) \end{pmatrix} \Rightarrow y(t) \text{ — реш.}$$

$$\frac{d}{dt} y = \begin{pmatrix} y_1 \\ \vdots \\ y_n \end{pmatrix}' = \begin{pmatrix} y_2 \\ \vdots \\ y_n \\ g(t, y_1, \dots, y_n) \end{pmatrix} = f(t, y)$$

$$(t_0, u^0, u^1, \dots, u^{n-1}) \in G$$

$$\begin{cases} u^{(n)} = g(t, u, u', \dots, u^{(n-1)}) \\ u(t_0) = u^0 \\ \dots \\ u^{(n-1)}(t_0) = u^{n-1} \end{cases} \longrightarrow \begin{cases} \frac{d}{dt} y = \begin{pmatrix} y_2 \\ \vdots \\ y_n \\ g(t, y_1, \dots, y_n) \end{pmatrix} \\ y(t_0) = \begin{pmatrix} u^0 \\ \vdots \\ u^{n-1} \end{pmatrix} \end{cases}$$

---
02.10.25

$$\frac{dy}{dt} = f(t, y)$$

Предполож...
1) $f(t, y) \in [НРЗБ]$
2) $f(t, y) \in [НРЗБ]$
$\exists L$ [НРЗБ]

Пусть $y_0$ [НРЗБ]
Обозначим:
$y_1 = y(t)$
$$\frac{dy}{dt} = f(t, y)$$
$$y(t_0) = y^0$$

### Опр. Пусть:
1) $y^1(t)$
2) $y^2(t)$
3) [НРЗБ]
Т.е. либо
4) $y^1(t) = y^2(t)$
Тогда $y^2(t)$ [НРЗБ] $y^1(t)$
Аналогично [НРЗБ]

### Опр. Решение [НРЗБ]

 --- 

photo_2026-05-01 12.40.54 PM.jpeg -- 10

 --- 

# 02.10.25 лекция

## § 2 Непродолжаемые решения диф. ур.

$$ \frac{dy}{dt} = f(t, y) \quad (1) $$
$$ f: G \to \mathbb{R}^n, \text{ область } G \subset \mathbb{R}^{n+1} $$

### Предположение (☼)
- 1) $f(t, y) \in C(G)$
- 2) $f(t, y)$ локально липшицева по $y$ в $G$, т. е. $\forall$ компакта $K \subset G$ $\exists L(K) > 0 \quad \forall (t, y^1), (t, y^2) \in K \quad \| f(t, y^1) - f(t, y^2) \| \le L(K) \| y^1 - y^2 \|$

Пусть $Y_0 = \{ (t, y) \mid |t - t_0| \le T^0, \|y - y_0\| \le \rho \}$
$Y_0 \subset G \Rightarrow$ по Тм Пикара $\exists!$ решение, определённое при $|t - t_0| \le T^{**}, \quad T^{**} = \min \left\{ T^0, \frac{\rho}{F^0} \right\}$
$$ \begin{cases} \frac{dy}{dt} = f(t, y) \\ y(t_0) = y_0 \end{cases} $$

### Обозначим:
$y_1 = y(t_0 + T^{**})$ рассмотрим ЗК:
$$ \begin{cases} \frac{dy}{dt} = f(t, y) \\ y(t_0 + T^{**}) = y_1 \end{cases} $$

*Что тут происходит?*
*Сие зовётся „Пикарить“.*
*Берём правую точку (пересечение интегральной кривой с цилиндром) и строим там цилиндр ещё один.*

### Опр.
Пусть:
- 1) $y^1(t)$ — реш (1), опред на $\langle t_-^1, t_+^1 \rangle$
- 2) $y^2(t)$ — решение (1), определенное на $\langle t_-^2, t_+^2 \rangle$
- 3) $\langle t_-^1, t_+^1 \rangle \subset \langle t_-^2, t_+^2 \rangle$
Т. е. либо $t_+^2 > t_+^1$, либо $\begin{cases} \langle t_-^1, t_+^1 \rangle = [t_-^1, t_+^1) \\ \langle t_-^2, t_+^2 \rangle = [t_-^1, t_+^1] \end{cases}$
- 4) $y^1(t) = y^2(t)$ при $t \in \langle t_-^1, t_+^1 \rangle$

Тогда $y^2(t)$ называется **продолжением** решения $y^1(t)$ вправо; $y^1(t)$ называется **продолжаемым** вправо.
Аналогично влево.

### Опр.
Решение, не имеющее продолжений вправо/влево, зовётся **непродолжаемым**.

 --- 

photo_2026-05-01 12.40.56 PM.jpeg -- 11

 --- 

# Лемма 1

Пусть выполнено предположение (☀): и справедливо следующее:

- 1) $y^1(t)$ — реш (1), опред на $(t^1_-, t^1_+)$
- 2) $y^2(t)$ — реш (1), опред на $(t^2_-, t^2_+)$
- 3) $(t^1_-, t^1_+) \cap (t^2_-, t^2_+) = (a, b)$
- 4) $\exists t_0 \in (a, b) \mid y^1(t_0) = y^2(t_0)$

$\Rightarrow y^1(t) = y^2(t)$ при $t \in (a, b)$

### Доказательство
$\square$: От противного.
Предположим $\exists t^* \in (a, b) \mid y^1(t^*) \neq y^2(t^*)$. Считаем $t^* > t_0$
Введём: $M = \{ t \in [t_0, t^*] \mid y^1(t) = y^2(t) \}$
$M$ — непусто т.к. $t_0 \in M$

1) Покажем, что $M$ — замкнуто. Пусть $\{ t_k \}$ — послед-ть $t_k \in M$, при этом $\exists \lim_{k \to \infty} t_k = \bar{t}$
$$y^1(t_k) - y^2(t_k) = 0$$
в силу непрерывности решения получим: $y^1(\bar{t}) - y^2(\bar{t}) = 0 \Rightarrow \bar{t} \in M$

2) $M$ — замкнутое $\Rightarrow \sup M \in M$
$\forall t \in M \quad t < t^* \Rightarrow \sup M < t^*$
обозначим $\bar{t}^0 = \sup M$
$y^1(\bar{t}^0) = y^2(\bar{t}^0) = y^0$

Рассмотрим ЗК:
$$\begin{cases} \frac{dy}{dt} = f(t,y) \\ y(\bar{t}^0) = y^0 \end{cases} \Rightarrow \exists! \text{ реш. определённое при } |t - \bar{t}^0| < \Delta T_0 \Rightarrow$$
$$\Rightarrow y^1(t) = y^2(t) \text{ при } t \in [\bar{t}^0 - \Delta T_0, \bar{t}^0 + \Delta T_0] \cap (a, b) \Rightarrow$$
$$\Rightarrow \bar{t}^0 \neq \sup M \Rightarrow \text{противоречие } \blacksquare$$

 --- 

photo_2026-05-01 12.40.58 PM.jpeg -- 12

 --- 

$$\begin{cases} \frac{dy}{dt} = f(t, y) \\ y(t_0) = y_0 \end{cases} \quad (2)$$

### Теорема (о существовании и единственности непродолжаемого решения)
Пусть выполнено предположение $(\text{☀})$ и $(t_0, y_0) \in G \implies$
$\implies \exists !$ непродолжаемое решение ЗК $(2)$

### Доказательство:
Обозначим за $Y$ — множество всех решений ЗК $(2)$
- $T^+$ — множество всех правых концов интервала сущ. реш. из $Y$
- $T^-$ — множество всех левых концов -//- -//-

$t_- = \inf T^-$; $t_+ = \sup T^+$; $(t_-, t_+)$ — интервал существования непродолжаемого решения.

Пусть $t \in (t_-, t_+)$. Как определить значение непродолжаемого решения в этой точке?
$y(t) - ?$

$\exists \tilde{y}(t) \in Y$, опред. на $(\tilde{t}_-, \tilde{t}_+), t \in (\tilde{t}_-, \tilde{t}_+)$. Положим $y(t) = \tilde{y}(t)$.
Покажем, что такое определение непродолжаемого решения корректно, т.е. не зависит от выбора $\tilde{y}(t)$.

Пусть $\tilde{\tilde{y}}(t) \in Y$, определено на $(\tilde{\tilde{t}}_-, \tilde{\tilde{t}}_+), t \in (\tilde{\tilde{t}}_-, \tilde{\tilde{t}}_+)$.
Т.к. $t_0 \in (\tilde{t}_-, \tilde{t}_+)$ и $t_0 \in (\tilde{\tilde{t}}_-, \tilde{\tilde{t}}_+)$ и $\tilde{y}(t_0) = \tilde{\tilde{y}}(t_0) = y_0$, то по пред. [НРЗБ: о ед.] $\tilde{y}(t) = \tilde{\tilde{y}}(t)$. [НРЗБ: зачеркнуто]

# 09.10.25 лекция

### Теорема (о покидании компакта)
Пусть выполнено предположение $(\text{☀})$ и справедливы следующие условия:
1) $y(t)$ — непродолжаемое решение (1), определённое на $(t_-, t_+)$;
2) $K \subset G$ — непустой связный компакт;
3) $\gamma = \{ (t, y(t)) \mid t \in (t_-, t_+) \}$ — интегральная кривая и $\gamma \cap K \neq \varnothing$;
$\implies \exists t_1, t_2 \mid \forall t \in (t_-, t_+) \setminus [t_1, t_2], (t, y(t)) \notin K$.

### Доказательство:
Выберем число $d > 0$, $dist(\partial G, \partial K) \ge d$.
Построим компакт: $K' = \{ (t, y) \in G \mid dist((t, y), K) \le \frac{d}{2} \} \subset G$.
Рассмотрим цилиндр: $V_{\frac{d}{4}}(t_0, y_0) = \{ (t, y) \mid |t - t_0| \le \frac{d}{4}, \|y - y_0\| \le \frac{d}{4} \}$.
Тогда $\forall (t_0, y_0) \in K \implies V_{\frac{d}{4}}(t_0, y_0) \subset K'$.

 --- 

photo_2026-05-01 12.40.59 PM.jpeg -- 13

 --- 

1) Рассмотрим ЗК (2) $\frac{dy}{dt} = f(t, y), y|_{t=t_0} = y_0; (t_0, y_0) \in K$

Из (-*-) $f(t, y) \in C(\bar{U}(t_0, y_0))$; $f(t, y)$ — липшицева по $y$ в $\bar{U}(t_0, y_0)$

Тогда выполнены условия Тн Пикара $\Rightarrow$ ЗК $\exists!$ решение, определенное на $[t_0 - T_0, t_0 + T_0]$, $T_0 = \min \left\{ \frac{d}{4}, \frac{d}{4F} \right\}$, $F = \max_{(t, y) \in \bar{U}(t_0, y_0)} \|f(t, y)\|$

Тогда ЗК имеет решение, определенное на $[t_0 - T_0^*, t_0 + T_0^*]$, где $T_0^* = \min \left\{ \frac{d}{4}, \frac{d}{4F^*} \right\}$, $F^* = \max_{(t, y) \in K} \|f(t, y)\|$, $T_0^* \le T_0$

2) Покажем, что $\forall t \in (t_2, t_+) \quad (t, y(t)) \notin K$
$t_2 = t_+ - T_0^*$
$\forall t \in (t_+ - T_0^*, t_+) \quad (t, y(t)) \notin K$ От противного:
$\exists \tilde{t} \mid (t_2 + \tilde{t}, y(t_2 + \tilde{t})) \in K$. Рассмотрим задачу Коши:
$$ \begin{cases} \frac{dy}{dt} = f(t, y) \\ y|_{t = t_2 + \tilde{t}} = y(t_2 + \tilde{t}) \end{cases} \text{ с начальными данными } \begin{cases} t_0 = t_2 + \tilde{t} \\ y_0 = y(t_2 + \tilde{t}) \end{cases} $$
$\Rightarrow$ из шага (1) получили, что решение $y(t)$ определено при $[t_2 + \tilde{t} - T_0^*, t_2 + \tilde{t} + T_0^*]$
Тогда $t_2 + \tilde{t} + T_0^* \le t_+$
$t_+ + \tilde{t} \le t_+ \Rightarrow \tilde{t} \le 0$ — противоречие

3) $t_-$ находится аналогично и Тн [НРЗБ: доказана] $\blacksquare$

### Тн (о поведении решения в полосе)
Пусть $G = \{ t \in (a, b), y \in \mathbb{R}^n \}$ и выполнено предположение (-*-). Рассмотрим непродолжаемое решение $y(t)$ системы (1), определенное на $(t_-, t_+)$
$\Rightarrow$ а) либо $(t_+ = b)$, либо $(\|y(t)\| \to \infty \text{ при } t \to t_+ - 0)$
б) либо $(t_- = a)$, либо $(\|y(t)\| \to \infty \text{ при } t \to t_- + 0)$

### Доказательство:
Докажем пункт а. Т.е. покажем, что если $t_+ < b$, то $\|y(t)\| \to \infty$ при $t \to t_+ - 0$.
Выберем $c$ и $d$: $a < c < t_+ < d < b$
Рассмотрим семейство компактов: $K(\rho) = \{ t \in [c, d] \mid \|y\| \le \rho \}, \rho > 0$
$\gamma = \{ (t, y(t)), t \in (t_-, t_+) \}$
Имеем два случая:

 --- 

photo_2026-05-01 12.41.00 PM.jpeg -- 14

 --- 

# [НРЗБ: Продолжение доказательства]

а) $\partial \Omega \cap K(\rho) = \emptyset \Rightarrow \|y(t)\| > \rho, t \in (t_-, t_+)$

б) $\partial \Omega \cap K(\rho) \neq \emptyset \Rightarrow$ по Тн. о покидании компакта $\exists t_2, \forall t \in (t_2, t_+) (t, y(t)) \notin K_{\rho} \Rightarrow \forall t \in (\max \{C, t_2\}, t_+) \|y(t)\| > \rho$

Устремив $\rho_k \to \infty$ получим, что $\|y(t)\| \to +\infty, t \to t_+ - 0$

С пунктом [НРЗБ: а] аналогично

## Тн (Уитнера) (без док-ва)

Пусть выполнено предположение $(\text{-}\circleddash\text{-})$ (при этом $G = \{t \in (a, b), y \in \mathbb{R}^n \}$) и справедлива оценка $\|f(t, y)\| \leq \varphi(t) \cdot g(\|y\|)$, $\varphi \in C(a, b)$

$$\int_{s}^{+\infty} \frac{du}{g(u)} = +\infty$$

$g(u)$ — непрерывная функция, $\exists s_0 > 0 \mid \forall \rho > \rho_0$

$\Rightarrow$ любое непродолжаемое решение (1) определено до $b$ (т. е. $t_+ = b$)

## Рассмотрим подкласс диффуров (автономные ур-е)

$$\frac{dy}{dt} = f(y) \quad (3)$$

Предположение $(\mathcal{D})$:

1) $f(y) \in C^1(\mathbb{R}^n)$ ($f(t, y) \in C^1(B_r)$), $B_r = \{y \in \mathbb{R}^n \mid \|y\| \leq r \}$
2) $f(0) = 0$

из 2 вытекает, что $y(t) \equiv 0$ — решение (3)

### Опр.

Функция Ляпунова — функция $h(y)$, определённая в шаре $B_r = \{ \|y\| < r \}$, удовлетворяет след. свойствам:

1) $h(y) \in C^1(B_r)$
2) $h(y) \geq 0, y \in B_r$
   $h(y) = 0 \Leftrightarrow y = 0$
3) $\langle \nabla h(y), f(y) \rangle \leq 0, y \in B_r$

### Тн (Ляпунова об устойчивости)

Пусть выполнено предположение $(\mathcal{D})$ и $\exists$ функция Ляпунова, определенная в $B_r$

$\Rightarrow \exists \epsilon \in (0, r) \mid \forall$ непрод. реш. ЗК $\begin{cases} \frac{dy}{dt} = f(y) \\ y(t_0) = y_0 \end{cases}$ у которого $\|y_0\| < \epsilon$ определено до $+\infty$ ($t_+ = +\infty$)

 --- 

photo_2026-05-01 12.41.01 PM.jpeg -- 15

 --- 

# 16.10.25 лекция

## Тн (Ляпунова)

### Теорема
Пусть выполнено предположение $(D)$ и $\exists$ функция Ляпунова $\Rightarrow \exists \gamma_0 \ \forall y_0: \|y_0\| < \gamma_0$ непродолж. решение $y(t)$ ЗК
$$\begin{cases} \frac{dy}{dt} = f(y) \\ y(t_0) = y_0 \end{cases}$$
определено при всех $t \ge t_0$.

### Доказательство
- Введем функции:
$$m(\rho) = \min_{\|y\|=\rho} h(y)$$
$$M(\rho) = \max_{\|y\| \le \rho} h(y)$$

Очевидно, что $m(0) = M(0) = 0$, $m(\rho) > 0, M(\rho) > 0$ при $\rho > 0$.
$m(\rho), M(\rho)$ — непрерывные.

Выберем $\gamma_0 > 0$ так, чтобы $M(\gamma_0) < m(\frac{r}{2})$.

1) Пусть $y_0 : \|y_0\| < \gamma_0 \Rightarrow \|y_0\| < \frac{r}{2}$.
Рассмотрим $V = \{ (t, y) \in \mathbb{R}^{n+1} \mid |t - t_0| \le \frac{r}{2F}, \|y - y_0\| \le \frac{r}{2} \}$,
$F = \max_{\|y\| \le r} \|f(y)\|$.

Тогда по Тн Пикара ЗК (3) имеет решение единственное определённое при $t \in [t_0, t_0 + T_0]$, $T_0 = \min \{ \frac{r}{2F}, \frac{r/2}{F} \} = \frac{r}{2F}$.

$$\|y\| \le \|y - y_0\| + \|y_0\| < \frac{r}{2} + \frac{r}{2} = r$$

Имеем решение $y(t)$ определённое при $t \in [t_0, t_0 + T_0]$.
Рассмотрим $h(y(t))$. Получим
$$\frac{d}{dt} h(y(t)) = \frac{d}{dt} h(y_1(t), \dots, y_n(t)) = \sum_{i=1}^n \frac{\partial h}{\partial y_i} \Big|_{y=y(t)} \frac{dy_i}{dt} = \sum_{i=1}^n \frac{\partial h}{\partial y_i} \Big|_{y=y(t)} f_i(y(t)) = (\nabla h(y(t)), f(y(t))) \le 0$$

$\|y(t)\| \le \|y(t) - y_0\| + \|y_0\| < \frac{r}{2} + \frac{r}{2} = r \Rightarrow \|y(t)\| < r$.
Тогда $h(y(t))$ — невозрастающая $\Rightarrow h(y(t)) \le h(y_0) \le M(\gamma_0) < m(\frac{r}{2})$ при $t \in [t_0, t_0 + T_0]$.
Из свойств на опр. $m(\frac{r}{2}) \Rightarrow \|y(t)\| < \frac{r}{2}$ при $t \in [t_0, t_0 + T_0] \Rightarrow \|y(t_0 + T_0)\| < \frac{r}{2}$.

 --- 

photo_2026-05-01 12.41.02 PM.jpeg -- 16

 --- 

# Лекция: Устойчивость по Ляпунову и зависимость решений от параметров

2) Рассмотрим цилиндр
$$ y_2 = \left\{ (t, y) \in \mathbb{R}^{n+1} \mid |t - (t_0 + T_0)| \le \frac{r}{2F} \right\} $$
$\implies$ по Тн. Пикара ЗК
$$ \begin{cases} \frac{dy}{dt} = f(y) \\ y|_{t=t_0 + T_0} = y(t_0 + T_0) \end{cases} $$
имеет единственное решение, определённое при $t \in [t_0, t_0 + 2T_0]$, при этом $\| y(t) - y(t_0 + T_0) \| \le \frac{r}{2}$. При этом $\| y(t) \| < r$.
Повторяя выше написанные рассуждения получим, что $h(y(t))$ не возрастает при $t \in [t_0, t_0 + 2T_0)$.
$$ h(y(t_0 + 2T_0)) \le h(y_0) \le M(r_0) < m\left(\frac{r}{2}\right) \implies \| y(t_0 + 2T_0) \| < \frac{r}{2} $$
Повторяя рассуждения получим, что решение определено при всех $t \ge t_0 \square$.

### Следствие (Ляпунов)
Пусть выполнены условия пред. Тн и выполнено след. условие:
3') $(\nabla h, f(y)) < 0, \ y \in B_r \setminus \{0\}$
$\implies \exists \eta_0 > 0 \quad \forall y_0 : \| y_0 \| < \eta_0$ решение ЗК
$$ \begin{cases} \frac{dy}{dt} = f(y) \\ y|_{t=t_0} = y_0 \end{cases} $$
такое, что $\| y(t) \| \xrightarrow[t \to +\infty]{} 0$.

## § 3 Непрерывная зависимость решений от параметров и начальных данных
$$ \begin{cases} \frac{dy}{dt} = f(t, y, \mu) \\ y|_{t=t_0} = y_0 \end{cases} \quad (1) $$
$(t, y, \mu) \in B$, $B \subset \mathbb{R}^{n+k+1}$
$$ y = \begin{pmatrix} y_1 \\ \vdots \\ y_n \end{pmatrix}, \quad \mu = \begin{pmatrix} \mu_1 \\ \vdots \\ \mu_k \end{pmatrix} $$

Предположение $(\Phi)$ [НРЗБ: или звезда хаоса из моих картинок]
- 1) $f(t, y, \mu) \in C(B)$
- 2) $f(t, y, \mu)$ локально липш. по $y$ в $B$.

Обозначим через $(t_-(\mu), t_+(\mu))$ интервал определения (существования) непрод. решения (1).
$y(t, \mu)$ — непрод. реш. ЗК (1).
Введём мн-во $\mathfrak{M} = \{ (t, \mu) \mid (t_0, y_0, \mu) \in B, \ t \in (t_-(\mu), t_+(\mu)) \}$.

### Тн №1
Пусть выполнено предположение $(\Phi) \implies \mathfrak{M}$ — открытое и $y(t, \mu) \in C(\mathfrak{M})$.

 --- 

photo_2026-05-01 12.41.03 PM.jpeg -- 17

 --- 

1) Докажем, что $\mathfrak{M}$ — открытое

Пусть $(t^*, \mu^*) \in \mathfrak{M}$, покажем, что некоторая окрестность принадлежит $\mathfrak{M}$
для определенности рассмотрим случай $t^* > t_0$. Установим, что
$\forall t_1 \in (t^*, t_+(\mu^*))$
$\exists m, \eta > 0 : [t_0, t_1] \times \{ \|\mu - \mu^*\| < m \} \subset \mathfrak{M}$
(окр-ть $(t^*, \mu^*)$, компакт)

Очевидно, что непродолжаемое реш. $y(t, \mu^*)$ определено при $t \in [t_0, t_1]$
Рассмотрим кривую
$$S = \{ (t, y(t, \mu^*), \mu^*) \mid t \in [t_0, t_1] \}$$
$$\Pi = \{ (t, y, \mu) \mid t \in [t_0, t_1], \|y - y(t, \mu^*)\| \le \rho, \|\mu - \mu^*\| \le m \}$$
выберем $\rho, m \mid \Pi \subset B$. Пусть $\mu : \|\mu - \mu^*\| < m$ ($(t_0, y_0, \mu) \in \Pi$)
Пересечение $\Pi$ и гиперплоскости $\mu = c$ — компакт $\Rightarrow$
$\Rightarrow$ по Тн о покидании компакта непрод. реш. $y(t, \mu)$ $\exists t_+^* :$
$\forall t \in [t_0, t_+(\mu)) \quad (t, y(t, \mu)) \notin \text{пересек}$
$\Rightarrow \forall t \in (t_-^*, t_+(\mu)), (t, y(t, \mu), \mu) \in \Pi$
обозначим за $t > t_0$

# 23.10.25 лекция

$$\begin{cases} \frac{dy}{dt} = f(t, y, \mu) \\ y(t_0) = y_0 \end{cases} \quad (1)$$

### Предположение ($\Phi$)
- 1) $f(t, y, \mu) \in C(B)$
- 2) $f(t, y, \mu)$ локально липшицева по $y$ в $B$

$y(t, \mu)$ — реш (1), опр на $(t_-(\mu), t_+(\mu))$
$$\mathfrak{M} = \{ (t, \mu) : (t_0, y_0, \mu) \in B, t \in (t_-(\mu), t_+(\mu)) \}$$

 --- 

photo_2026-05-01 12.41.04 PM(1).jpeg -- 18

 --- 

### Теорема
Пусть выполнено предположение 2, тогда:
- а) $\mathfrak{M}$ — открыто
- б) $y(t, \mu) \in C(\mathfrak{M})$

### Доказательство
$\forall t \in [t_0, t^*] \mid \|y(t, \mu) - y(t, \mu^*)\| < \rho$
$y(t, \mu) - y(t, \mu^*)$ — решение системы:
$$
\begin{cases} 
\frac{d}{dt} (y(t, \mu) - y(t, \mu^*)) = f(t, y(t, \mu), \mu) - f(t, y(t, \mu^*), \mu^*) \\ 
y(t_0, \mu) - y(t_0, \mu^*) = 0 
\end{cases}
$$

$$y(t, \mu) - y(t, \mu^*) = \int_{t_0}^t (f(s, y(s, \mu), \mu) - f(s, y(s, \mu^*), \mu^*)) \, ds \Rightarrow$$
$$\Rightarrow y(t, \mu) - y(t, \mu^*) = \int_{t_0}^t (f(s, y(s, \mu), \mu^*) - f(s, y(s, \mu^*), \mu^*)) \, ds + \int_{t_0}^t (f(s, y(s, \mu), \mu) - f(s, y(s, \mu), \mu^*)) \, ds \Rightarrow$$
$$\Rightarrow \|y(t, \mu) - y(t, \mu^*)\| \le \int_{t_0}^t \|f(s, y(s, \mu), \mu^*) - f(s, y(s, \mu^*), \mu^*)\| \, ds + \int_{t_0}^t \|f(s, y(s, \mu), \mu) - f(s, y(s, \mu), \mu^*)\| \, ds \Rightarrow$$
$$\Rightarrow \|y(t, \mu) - y(t, \mu^*)\| \le \int_{t_0}^t L \|y(s, \mu) - y(s, \mu^*)\| \, ds + \int_{t_0}^t \|f(s, y(s, \mu), \mu) - f(s, y(s, \mu), \mu^*)\| \, ds$$

### Вспомогательная лемма
### Лемма Гронуолла
Пусть $\varphi(t) \in C(t_1, t_2)$; $\varphi(t) \ge 0$ и $u(t) \in C(t_1, t_2)$.
$\exists t^* \in (t_1, t_2) \mid \forall t > t^* \quad 0 \le u(t) \le \int_{t^*}^t (L u(s) + \varphi(s)) \, ds, \quad L \ge 0$
$\Rightarrow u(t) \le \int_{t^*}^t e^{L(t-s)} \varphi(s) \, ds, \quad t > t^*$

### Доказательство
$v(t) = \int_{t^*}^t (L u(s) + \varphi(s)) \, ds$. Получим $0 \le u(t) \le v(t)$, $v(t^*) = 0$
$$\frac{d}{dt} v(t) = L u(t) + \varphi(t) \le L v(t) + \varphi(t)$$
$$\frac{d}{dt} v(t) - L v(t) \le \varphi(t) \quad | \cdot e^{-Lt}$$
$$\frac{d}{dt} (e^{-Lt} v(t)) \le e^{-Lt} \varphi(t)$$

 --- 

photo_2026-05-01 12.41.05 PM(1).jpeg -- 19

 --- 

### Тн
Пусть выполнено предположение $(\sigma) \Rightarrow$
- а) $\mathfrak{M}_0$ - открыто
- б) $y(t, t_0, y_0) \in C(\mathfrak{M}_0)$

### Доказательство
Введем $x(t, t_0, y_0) = y(t, t_0, y_0) - y_0$. Тогда $x(t, t_0, y_0)$ — решение
$$
\begin{cases}
\frac{dx}{dt} = f(t, x + y_0) \\
x(t_0) = 0
\end{cases}
$$
Замена $\tilde{t} = t - t_0$, $z(\tilde{t}, t_0, y_0) \big|_{\tilde{t} = t - t_0} = x(t, t_0, y_0)$
$$
\frac{dz}{d\tilde{t}} \bigg|_{\tilde{t} = t - t_0} = \frac{dx}{dt} (t, t_0, y_0)
$$
$z(\tilde{t}, t_0, y_0)$ — решение
$$
\frac{dz}{d\tilde{t}} = f(\tilde{t} + t_0, z + y_0), \quad z \big|_{\tilde{t}=0} = 0
$$
применяем ранее доказанную Тн. $\blacksquare$

## §4 Дифференциальная зависимость решений от параметров и начальных данных
$$
\begin{cases}
\frac{dy}{dt} = f(t, y, \mu) \\
y \big|_{t=t_0} = y_0
\end{cases} \quad (1)
$$
$f: B \to \mathbb{R}^n$
$B$ — область, $B \subset \mathbb{R}^{n+k+1}$

### Предположение (*)
- 1) $f(t, y, \mu) \in C(B)$
- 2) $\exists \frac{\partial f}{\partial y_j}, \frac{\partial f}{\partial \mu_i} \in C(B) \quad j=1, \dots, n; \quad i=1, \dots, k$

$\mathfrak{M} = \{ (t, \mu) \mid (t_0, y_0, \mu) \in B, t \in (t_-(\mu), t_+(\mu)) \}$

### Тн
Пусть выполнено предположение (*) $\Rightarrow$
- а) $\exists \frac{\partial y}{\partial \mu_i} \in C(\mathfrak{M}), \quad i=1, \dots, k$
- б) Вектор-функция $v^i(t, \mu) = \begin{pmatrix} \frac{\partial y_1}{\partial \mu_i} \\ \vdots \\ \frac{\partial y_n}{\partial \mu_i} \end{pmatrix}$ — решение $i=1, \dots, k$

 --- 

photo_2026-05-01 12.41.05 PM.jpeg -- 20

 --- 

$$ e^{-Lt} v(t) - e^{-Lt^*} v(t^*) \le \int_{t^*}^t e^{-Ls} \psi(s) ds $$
$$ u(t) \le v(t) \le e^{Lt} \int_{t^*}^t e^{-Ls} \psi(s) ds $$

Пользуясь только что доказанной леммой:
$$ \|y(t, \mu) - y(t, \mu^*)\| \le \int_{t^*}^t e^{L(t-s)} \|f(s, y(s, \mu), \mu) - f(s, y(s, \mu), \mu^*)\| ds \le $$
$$ \le \max_{(t, y, \mu) \in \Pi} \|f(t, y, \mu) - f(t, y, \mu^*)\| \int_{t^*}^t e^{L(t-s)} ds $$
$$ \|y(t, \mu) - y(t, \mu^*)\| \le \frac{1}{L} (e^{L(t-t^*)} - 1) \max_{(t, y, \mu) \in \Pi} \|f(t, y, \mu) - f(t, y, \mu^*)\| $$

$\exists m_0 \mid m = m_0$ в $\Pi$ $\|y(t, \mu) - y(t, \mu^*)\| \le \delta$ при $t \in [t_a, t_b]$.
Тогда $[t_a, t_b] \times [\mu^* - m_0, \mu^* + m_0] \in \mathfrak{M}$.
окрестность $(t^*, \mu^*) \Rightarrow \mathfrak{M}$ — открыто.

В силу Тк Кантора и равн. непр. [НРЗБ: f на П] тогда уменьшая $m$ так [НРЗБ: что] норма также будет $\to 0$.

б) $y(t, \mu) \in C(\mathfrak{M})$
Нам нужно показать, что $\|y(t, \mu) - y(t^*, \mu^*)\| \xrightarrow[\substack{t \to t^* \\ \mu \to \mu^*}]{} 0$

$$ \|y(t, \mu) - y(t^*, \mu^*)\| \le \underbrace{\|y(t, \mu) - y(t^*, \mu)\|}_{\downarrow_{t \to t^*}} + \underbrace{\|y(t^*, \mu) - y(t^*, \mu^*)\|}_{\downarrow_{\mu \to \mu^*}} $$

### Задача Коши
\begin{cases} \frac{dy}{dt} = f(t, y) \\ y(t_0) = y_0 \end{cases} (2)
$f: G \to \mathbb{R}^n$, $G \subset \mathbb{R}^{n+1}$

### Предположение ($\sigma$)
- 1) $f(t, y) \in C(G)$
- 2) $f(t, y)$ — локально липшицева по $y$ в $G$
- 3) (2) имеет единственное непродолжаемое решение $y(t, t_0, y_0)$, определенное на $(t_-(t_0, y_0), t_+(t_0, y_0))$

$$ \mathfrak{M}_0 = \{ (t, t_0, y_0) \mid (t_0, y_0) \in G, t \in (t_-(t_0, y_0), t_+(t_0, y_0)) \} $$

 --- 

photo_2026-05-01 12.41.06 PM.jpeg -- 21

 --- 

$$\begin{cases} \frac{dv}{dt} = A(t, \mu) v + h^j(t, \mu) \\ v(t_0) = 0 \end{cases}$$ — система в вариациях Пуанкаре

$$A(t, \mu) = \left. \begin{pmatrix} \frac{\partial f_1}{\partial y_1} & \dots & \frac{\partial f_1}{\partial y_n} \\ \vdots & \ddots & \vdots \\ \frac{\partial f_n}{\partial y_1} & \dots & \frac{\partial f_n}{\partial y_n} \end{pmatrix} \right|_{y=y(t,\mu)} ; \quad h^j(t, \mu) = \left. \begin{pmatrix} \frac{\partial f_1}{\partial \mu_j} \\ \vdots \\ \frac{\partial f_n}{\partial \mu_j} \end{pmatrix} \right|_{y=y(t,\mu)} ; \quad y(t, \mu) - [НРЗБ: реш.]$$

в) $\exists \frac{\partial y}{\partial \mu_j}, \frac{\partial^2 y}{\partial \mu_j \partial t} \in C(\mathfrak{M})$

### Доказательство:
(30.10.25 лекция)

Рассмотрим случай $l=1$

$y(t, \mu^*)$ — решение ЗК(1) при $\mu = \mu^*$ определенным на $(t_-(\mu^*), t_+(\mu^*))$

Выберем $[t_1, t_2] \subset (t_-(\mu^*), t_+(\mu^*)) \mid t_0 \in [t_1, t_2]$

$\Rightarrow y(t, \mu) \in C(\mathfrak{M}), \mathfrak{M}$ — откр.

Выберем $m_0 > 0 \mid [t_1, t_2] \times \{ \|\mu - \mu^*\| \le m_0 \} \subset \mathfrak{M}$ и
при $\|\mu - \mu^*\| \le m_0 \quad \forall t \in [t_1, t_2] \quad \|y(t, \mu) - y(t, \mu^*)\| \le \rho$

Построим $\Pi = \{ (t, y, \mu) \mid t \in [t_1, t_2]; \|y(t, \mu^*) - y\| \le \rho, \|\mu - \mu^*\| \le m_0 \}$

$\Pi \subset B$

Возьмём $\bar{\mu} \mid \|\bar{\mu} - \mu^*\| \le \frac{m_0}{2}; \mu = \bar{\mu} + \tau e_j \quad (\tau \in [-\frac{m_0}{2}, \frac{m_0}{2}], e_j - j\text{-базис})$

Покажем, что $\exists \frac{\partial y}{\partial \mu_j} (t, \bar{\mu}) = \lim_{\tau \to 0} \frac{y(t, \bar{\mu} + \tau e_j) - y(t, \bar{\mu})}{\tau}$

### Лемма Адамара

Пусть $g(u, v) \in C(U \times V); g: U \times V \to \mathbb{R}^n, U \subset \mathbb{R}^m$ — выпуклая область, $V \subset \mathbb{R}^k; \exists \frac{\partial g}{\partial v_i} \in C(U \times V), i = 1, \dots, k$

$\Rightarrow g(u, v^1) - g(u, v^2) = A(u, v^1, v^2) (v^1 - v^2)$

Матрица $A(u, v^1, v^2)$ непрерывна по совокупности переменных.

### Доказательство:

$$g(u, v^1) - g(u, v^2) = \int_0^1 \frac{d}{d\lambda} g(u, v^2 + \lambda(v^1 - v^2)) \, d\lambda =$$

$$= \int_0^1 \begin{pmatrix} \frac{\partial g_1}{\partial v_1}(u, w) & \dots & \frac{\partial g_1}{\partial v_k}(u, w) \\ \vdots & \ddots & \vdots \\ \frac{\partial g_n}{\partial v_1}(u, w) & \dots & \frac{\partial g_n}{\partial v_k}(u, w) \end{pmatrix} (v^1 - v^2) \, d\lambda \equiv$$

где $w = v^2 + \lambda(v^1 - v^2)$

$$\equiv \left( \int_0^1 \frac{\partial g}{\partial v} \Big|_{v = v^2 + \lambda(v^1 - v^2)} d\lambda \right) (v^1 - v^2)$$

(часть матрицы Якоби)

 --- 

photo_2026-05-01 12.41.07 PM.jpeg -- 22

 --- 

$$\ominus \int_0^1 \frac{\partial g}{\partial v} \Big|_{v = v^2 + z(v^1 - v^2)} dz (v^1 - v^2) = \int_0^1 A(u, v^1, v^2) dz (v^1 - v^2) \blacksquare$$

### Замечание
Заметим $\|\mu - \mu^*\| \le m_0$.

$y(t, \bar{\mu})$ — решение
$$\begin{cases} \frac{d}{dt} y(t, \bar{\mu}) = f(t, y(t, \bar{\mu}), \bar{\mu}) \\ y|_{t=t_0} = y_0 \end{cases}$$

$y(t, \bar{\mu} + \tau e_i)$ — реш.
$$\begin{cases} \frac{d}{dt} y(t, \bar{\mu} + \tau e_i) = f(t, y(t, \bar{\mu} + \tau e_i), \bar{\mu} + \tau e_i) \\ y|_{t=t_0} = y_0 \end{cases}$$

Вычтем одно из другого.

$$\frac{d}{dt} (y(t, \bar{\mu} + \tau e_i) - y(t, \bar{\mu})) = f(t, y(t, \bar{\mu} + \tau e_i), \bar{\mu} + \tau e_i) - f(t, y(t, \bar{\mu}), \bar{\mu}) =$$
$$= (f(t, y(t, \bar{\mu} + \tau e_i), \bar{\mu} + \tau e_i) - f(t, y(t, \bar{\mu}), \bar{\mu} + \tau e_i)) +$$
$$+ (f(t, y(t, \bar{\mu}), \bar{\mu} + \tau e_i) - f(t, y(t, \bar{\mu}), \bar{\mu})) = \star$$

[НРЗБ: зачеркнуто] $= \tilde{A}_1(t, \bar{\mu}, \tau) (y(t, \bar{\mu} + \tau e_i) - y(t, \bar{\mu}))$
[НРЗБ: зачеркнуто] $= \tilde{A}_2(t, \bar{\mu}, \tau) \tau$

$$\star = \tilde{A}_1(t, \bar{\mu}, \tau) (y(t, \bar{\mu} + \tau e_i) - y(t, \bar{\mu})) + \tilde{A}_2(t, \bar{\mu}, \tau) \tau$$

$$\tilde{A}_1(t, \bar{\mu}, \tau) = \int_0^1 \frac{\partial f}{\partial y} \Big|_{y = y(t, \bar{\mu}) + z(y(t, \bar{\mu} + \tau e_i) - y(t, \bar{\mu}))} dz =$$
$$= \int_0^1 \begin{pmatrix} \frac{\partial f_1}{\partial y_1} & \dots & \frac{\partial f_1}{\partial y_n} \\ \vdots & \ddots & \vdots \\ \frac{\partial f_n}{\partial y_1} & \dots & \frac{\partial f_n}{\partial y_n} \end{pmatrix} \Bigg|_{y = y(t, \bar{\mu}) + z(y(t, \bar{\mu} + \tau e_i) - y(t, \bar{\mu}))} dz \xrightarrow[\tau \to 0]{} A(t, \bar{\mu})$$

$$\tilde{A}_2(t, \bar{\mu}, \tau) = \int_0^1 \frac{\partial f}{\partial \mu_i} \Big|_{\mu = \bar{\mu} + z \tau e_i} dz = \int_0^1 \begin{pmatrix} \frac{\partial f_1}{\partial \mu_i} \\ \vdots \\ \frac{\partial f_n}{\partial \mu_i} \end{pmatrix} \Bigg|_{\mu = \bar{\mu} + z \tau e_i} dz \xrightarrow[\tau \to 0]{} h^i(t, \bar{\mu})$$

$$y(t_0, \bar{\mu} + \tau e_i) - y(t_0, \bar{\mu}) = 0$$

 --- 

photo_2026-05-01 12.41.08 PM.jpeg -- 23

 --- 

# Дифференцируемость решения по параметрам и начальным условиям

Вектор-функция
$$w(t, \bar{\mu}, \epsilon) = \frac{y(t, \bar{\mu} + \epsilon e_i) - y(t, \bar{\mu})}{\epsilon} \text{ — решение}$$

$$\begin{cases} \frac{d}{dt} w = \tilde{A}_1(t, \bar{\mu}, \epsilon) w + \tilde{A}_2(t, \bar{\mu}, \epsilon) \\ w|_{t=t_0} = 0 \end{cases}$$

Тут нужно заметить, что мы находимся в условиях Th из прошлого $\S$ из правила [НРЗБ: 1].
$\tilde{A}_1, \tilde{A}_2$ непр. $\Rightarrow w(t, \bar{\mu}, \epsilon)$ непр. по совокупности аргументов в силу Th из прошлого параграфа $\Rightarrow$
$\Rightarrow \exists \lim_{\epsilon \to 0} w(t, \bar{\mu}, \epsilon) = \frac{\partial y}{\partial \mu_i} (t, \bar{\mu})$
$$w(t, \bar{\mu}, 0) \text{ Пункт а) сюда!}$$

$\tilde{A}_1(t, \bar{\mu}, \epsilon) \xrightarrow[\epsilon \to 0]{} A(t, \bar{\mu})$
$\tilde{A}_2(t, \bar{\mu}, \epsilon) \xrightarrow[\epsilon \to 0]{} h^i(t, \bar{\mu})$
$v^i(t, \bar{\mu}) = w(t, \bar{\mu}, 0) = \left. \frac{\partial y}{\partial \mu_i} \right|_{\mu = \bar{\mu}}$ — реш.

$$\begin{cases} \frac{d v^i}{dt} = A(t, \mu) v^i + h^i(t, \mu) \\ v^i|_{t=t_0} = 0 \end{cases} \text{ Пункт б) сюда}$$

В силу б) $\Rightarrow \exists \frac{\partial^2 y}{\partial t \partial \mu_i} \in C(\mathfrak{M})$

$\frac{dy}{dt} (t, \mu) = f(t, y(t, \mu), \mu) \xrightarrow[\text{непр. диф-ма по } \mu]{\text{непр. диф. по } y \text{ и } \mu} \exists \frac{\partial^2 y}{\partial \mu_i \partial t} \in C(\mathfrak{M})$ $\blacksquare$

### Следствие
Пусть вып. $(*)$ $\Rightarrow \frac{\partial^2 y}{\partial \mu_i \partial t} = \frac{\partial^2 y}{\partial t \partial \mu_i}$

$$\begin{cases} \frac{dy}{dt} = f(t, y) \\ y|_{t=t_0} = \xi \end{cases} \text{ (2)}$$

$f: G \to \mathbb{R}^n$; область $G \subset \mathbb{R}^{n+1}$

Предположение $(\bar{t}_0, \bar{\xi}) \in G$
- 1) $f(t, y) \in C(G)$
- 2) $\exists \frac{\partial f}{\partial y_j} \in C(G), j=1, \dots, n$

$y(t, \xi)$ — реш. ЗК (2) опред. на $(t_-(\xi), t_+(\xi))$
$$\mathfrak{M}_0 = \{ (t, \xi) \mid (t_0, \xi) \in G, t \in (t_-(\xi), t_+(\xi)) \}$$

 --- 

photo_2026-05-01 12.41.09 PM.jpeg -- 24

 --- 

### Th
Пусть выполнено предп. $( *^0 ) \Rightarrow$

а) $\exists \frac{\partial y}{\partial \xi_i}, i=1, \dots, n$

б) $v^i(t, \xi) = \frac{\partial y}{\partial \xi_i}$ — реш.
$$
\begin{cases} 
\frac{dv}{dt} = A(t, \xi) v^i \\ 
v^i |_{t=t_0} = e_i 
\end{cases}
$$
- **система Пуанкаре в вариациях начальных данных**
$$A(t, \xi) = \left. \frac{\partial f}{\partial y} \right|_{y=y(t, \xi)}$$

### Док-во сами
$$
A = \left. \frac{\partial f}{\partial y} \right|_{y=y(t, \xi)} = 
\begin{pmatrix} 
\frac{\partial f_1}{\partial y_1} & \dots & \frac{\partial f_1}{\partial y_n} \\ 
\vdots & \ddots & \vdots \\ 
\frac{\partial f_n}{\partial y_1} & \dots & \frac{\partial f_n}{\partial y_n} 
\end{pmatrix}_{y=y(t, \xi)}
$$

в) $\exists \frac{\partial^2 y}{\partial t \partial \xi_i}, \frac{\partial^2 y}{\partial \xi_i \partial t} \in C(\Pi_0)$

# 06.11.25 лекции

### Следствие
Пусть вып. $( *^0 ) \Rightarrow \frac{\partial^2 y}{\partial t \partial \xi_i} = \frac{\partial^2 y}{\partial \xi_i \partial t}$

## Глава 2. Линейные дифференциальные уравнения
$$ \frac{dy}{dt} = A(t)y + h(t) \quad (1) $$
$$
y(t) = \begin{pmatrix} y_1(t) \\ \vdots \\ y_n(t) \end{pmatrix}, 
A(t) = \begin{pmatrix} a_{11}(t) & \dots & a_{1n}(t) \\ \vdots & \ddots & \vdots \\ a_{n1}(t) & \dots & a_{nn}(t) \end{pmatrix}, 
h(t) = \begin{pmatrix} h_1(t) \\ \vdots \\ h_n(t) \end{pmatrix}
$$

- Если $h(t) \equiv 0$, то (1) — **система линейных однородных дифференциальных уравнений** (1-го порядка) (линейная однородная система дифференциальных уравнений (1-го порядка)).
- Если $h(t) \not\equiv 0$, то (1) — **система линейных неоднородных дифференциальных уравнений** (1-го порядка) (линейная неоднородная система дифференциальных уравнений (1-го порядка)).

$$ u^{(n)} + a_1(t) u^{(n-1)} + \dots + a_n(t) u = \varphi(t) \quad (2) $$
$$ u^{(k)} = \frac{d^k u}{dt^k} $$
$$ (2) \sim \frac{d^n u}{dt^n} + a_1(t) \frac{d^{n-1} u}{dt^{n-1}} + \dots + a_n(t) u = \varphi(t) $$

- Если $\varphi(t) \equiv 0$, то (2) — **линейное однородное дифференциальное уравнение** $n$-го порядка.
- Если $\varphi(t) \not\equiv 0$, то (2) — **линейное неоднородное дифференциальное уравнение** $n$-го порядка.

 --- 

photo_2026-05-01 12.41.10 PM.jpeg -- 25

 --- 

# § 1 Линейные однородные системы дифференциальных уравнений

$$ \frac{dy}{dt} = A(t)y + h(t) \quad (1) $$

Система (1) — система вида $\frac{dy}{dt} = f(t, y)$
$f(t, y) = A(t)y + h(t) \in C((a, b) \times \mathbb{R}^n)$ из [НРЗБ]
$A(t) \in C(a, b); \quad h(t) \in C(a, b)$

Посмотрим на липшицевость:
$$ \| f(t, y^1) - f(t, y^2) \| \le L \| y^1 - y^2 \| $$
$$ \| A(t)y^1 + h(t) - (A(t)y^2 + h(t)) \| = \| A(t)y^1 - A(t)y^2 \| \le \underbrace{\| A(t) \|}_{\le L} \| y^1 - y^2 \| $$

$B$ — $n \times n$
$\| B \| = \sqrt{\lambda_{max}}$, где $\lambda_{max}$ — макс. с. з. матрицы $B^*B$
$\| B \| = \sup_{x \ne 0} \frac{\| Bx \|}{\| x \|} = \sup_{\| x \| = 1} \| Bx \| = \dots$

$$ \begin{cases} \frac{dy}{dt} = A(t)y + h(t) \\ y|_{t=t_0} = y^0 \end{cases} \quad (2) $$

### Теорема №1
Пусть $A(t) \in C(a, b), \quad h(t) \in C(a, b) \Rightarrow \forall y^0 \exists!$ решение ЗК (2), определенное на $(a, b)$ (док-во ранее было).

### Следствие
Пусть $A(t) \equiv A$, тогда решение ЗК (2) имеет вид:
$$ y(t) = e^{(t-t_0)A} y^0 + \int_{t_0}^t e^{(t-s)A} h(s) \, ds \text{ — формула Коши} $$
$$ e^{tA} = E + tA + \frac{t^2 A^2}{2!} + \frac{t^3 A^3}{3!} + \dots $$

### Следствие
$A(t) \equiv A, h(t) \equiv 0 \Rightarrow$ решение ЗК (2) имеет вид $y(t) = e^{(t-t_0)A} y^0$.

### Следствие
$A(t) \equiv A, h(t) \equiv 0 \Rightarrow$ все решения системы (1) имеют вид $y(t) = e^{tA} \vec{c}, \vec{c} = [НРЗБ: const]$.

$$ \frac{dy}{dt} = A(t)y \quad (3) $$

---

### Теорема [НРЗБ]
Пусть [НРЗБ] линейным [НРЗБ]

### Доказательство
Пусть $z(t) = [НРЗБ]$
Дано:
$$ \frac{d}{dt} y^1 = [НРЗБ] $$
$$ \frac{d}{dt} y^2 = [НРЗБ] $$
$$ \frac{d}{dt} z(t) = [НРЗБ] = \alpha_1 A [НРЗБ] $$

### Опр.
Вектор-функция $\sum_{i=1}^k c_i y^i(t)$ [НРЗБ]

### Пример 1
$$ y^1(t) = \begin{pmatrix} e^t \\ e^t \end{pmatrix} $$
$c_1 y^1(t) + [НРЗБ]$
$\det R = [НРЗБ]$

### Пример 2
$$ y^1(t) = \begin{pmatrix} t^2 \\ 0 \end{pmatrix}, y^2(t) = \begin{pmatrix} 0 \\ t^2 \end{pmatrix} $$
$c_1 y^1(t) + c_2 [НРЗБ]$
- а) $(0, 1)$
- б) $(-1, 0)$

 --- 

photo_2026-05-01 12.41.11 PM.jpeg -- 26

 --- 

# Th (о структуре множества решений) №2 (3)

Пусть $A(t) \in C(a, b) \Rightarrow$ множество всех решений образует (является) линейным пространством.

### Доказательство
Пусть $y^1(t), y^2(t)$ — решения (3). Покажем, что $\forall \alpha_1, \alpha_2$ $z(t) = \alpha_1 y^1(t) + \alpha_2 y^2(t)$ — решение (3).

Дано:
$$ \frac{d}{dt} y^1(t) \equiv A(t) y^1(t) $$
$$ \frac{d}{dt} y^2(t) \equiv A(t) y^2(t) $$

Надо:
$$ \frac{d}{dt} z(t) \equiv A(t) z(t) $$

$$ \frac{d}{dt} z(t) = \frac{d}{dt} (\alpha_1 y^1(t) + \alpha_2 y^2(t)) = \alpha_1 \frac{d}{dt} y^1(t) + \alpha_2 \frac{d}{dt} y^2(t) = $$
$$ = \alpha_1 A(t) y^1(t) + \alpha_2 A(t) y^2(t) = A(t) (\alpha_1 y^1(t) + \alpha_2 y^2(t)) = A(t) z(t) \blacksquare $$

### Опр.
Вектор-функции $y^1(t), \dots, y^k(t)$ называются лнз на $(a, b)$, если
$$ \sum_{i=1}^k c_i y^i(t) = 0, t \in (a, b) \Leftrightarrow c_1 = \dots = c_k = 0 $$

### Пример 1
$$ y^1(t) = \begin{pmatrix} e^t \\ e^t \end{pmatrix}; y^2(t) = \begin{pmatrix} e^{2t} \\ 2e^{2t} \end{pmatrix} $$
$$ c_1 y^1(t) + c_2 y^2(t) = 0 \sim \underbrace{\begin{pmatrix} e^t & e^{2t} \\ e^t & 2e^{2t} \end{pmatrix}}_{R} \begin{pmatrix} c_1 \\ c_2 \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \end{pmatrix} $$
$$ \det R = e^{3t} \neq 0 \Rightarrow c_1 = c_2 = 0 $$

### Пример 2
$$ y^1(t) = \begin{pmatrix} t^2 \\ 0 \end{pmatrix}; y^2(t) = \begin{pmatrix} t|t| \\ 0 \end{pmatrix} $$
$$ c_1 y^1(t) + c_2 y^2(t) = 0 \sim c_1 t^2 + c_2 t|t| = 0 $$
- а) $(0, 1)$ лз
- б) $(-1, 0)$ лз
- в) $(-1, 1)$ лнз

 --- 

photo_2026-05-01 12.41.12 PM.jpeg -- 27

 --- 

# Лекция (13.11.23)

### Тн 3 (о линейной зависимости решений)
Пусть $A(t) \in C(a, b)$ и $y^{(1)}(t), \dots, y^{(k)}(t)$ — решения (3). Предположим, что $\exists t^*$ | векторы $y^{(1)}(t^*), \dots, y^{(k)}(t^*)$ — лз; тогда $y^{(1)}(t), \dots, y^{(k)}(t)$ — лз на $(a, b)$.

**Доказательство:**
$\square$ Вектора $y^{(1)}(t^*), \dots, y^{(k)}(t^*)$ лз; $\exists c_1, \dots, c_k | \sum_{i=1}^k c_i^2 \neq 0$:
$$\sum_{i=1}^k c_i y^{(i)}(t^*) = 0$$
Из тн о структуре мн-ва решений имеем, что: $z(t) = \sum_{i=1}^k c_i y^{(i)}(t)$ — реш (3). При этом $z(t^*) = 0$, т.е. $z(t)$ — реш. ЗК:
$$\begin{cases} \frac{dz}{dt} = A(t)z \\ z|_{t=t^*} = 0 \end{cases} \Rightarrow z(t) = 0 \text{ (Тн. Пикара) } \Rightarrow y^{(1)}(t), \dots, y^{(k)}(t) \text{ лз на } (a, b) \quad \blacksquare$$

На полях:
$$\frac{dy}{dt} = A(t)y \quad (3)$$

---

### Тн 4
Пусть $A(t) \in C(a, b) \Rightarrow$ мн-во всех решений (3) образует (является) линейным пространством с $\dim = n$.

**Доказательство:**
$\square$ Нужно доказать, что размерность $= n$.
Пусть $y_1^0, \dots, y_n^0 \in \mathbb{R}^n$ — базис $\mathbb{R}^n$. Рассматриваем серию ЗК ($t_0 \in (a, b)$):
$$\begin{cases} \frac{dy}{dt} = A(t)y \\ y(t_0) = y_1^0 \end{cases} \mapsto y^{(1)}(t)$$
$$\dots$$
$$\begin{cases} \frac{dy}{dt} = A(t)y \\ y(t_0) = y_n^0 \end{cases} \mapsto y^{(n)}(t)$$
Покажем, что $y^{(1)}(t), \dots, y^{(n)}(t)$ лин. независимы на $(a, b)$.
$$\sum_{i=1}^n b_i y^{(i)}(t) = 0 \quad \forall t \in (a, b) \Rightarrow \sum_{i=1}^n b_i y^{(i)}(t_0) = 0 \sim \sum_{i=1}^n b_i y_i^0 = 0 \Rightarrow b_1 = b_2 = \dots = b_n = 0$$
Пусть $y(t)$ — решение (3) $\Rightarrow \exists c_1, \dots, c_n : \sum_{i=1}^n c_i y^{(i)}(t_0) = y(t_0) \Rightarrow z(t) = y(t) - \sum_{i=1}^n c_i y^{(i)}(t)$ — реш ЗК:
$$\begin{cases} \frac{dz}{dt} = A(t)z \\ z(t_0) = 0 \end{cases} \Rightarrow y(t) - \sum_{i=1}^n c_i y^{(i)}(t) = 0 \sim y(t) = \sum_{i=1}^n c_i y^{(i)}(t) \quad \blacksquare$$

---

### Опр.
**Фундаментальной системой решений (ФСР)** называется любая система из $n$ линейно незав. решений системы (3).

### Следствие
Пусть $\{y^{(i)}(t)\}_{i=1}^n$ — ФСР (3), тогда общее решение (3) имеет вид:
$$y(t) = \sum_{i=1}^n c_i y^{(i)}(t)$$

### Опр.
Пусть $\{y^{(1)}, \dots, y^{(n)}\}$ — ФСР (3). Составим матрицу $Y(t) = (y^{(1)}(t), \dots, y^{(n)}(t))$, она называется **матрицей решений** или **фундаментальной матрицей**.

### Следствие
Пусть $Y(t)$ — фундаментальная матрица системы (3), тогда общее решение имеет вид:
$$y(t) = Y(t) \cdot C, \quad C \in \mathbb{R}^n$$

### Следствие
Пусть $Y(t)$ — ФМ системы (3), тогда решение ЗК с условием $y(t_0) = y_0$ имеет вид:
$$y(t) = Y(t) Y^{-1}(t_0) y_0$$

---

### Тн 5 (о связи ФМ)
Пусть $A(t) \in C(a, b)$, $Y_1(t)$ и $Y_2(t)$ — две ФМ системы (3). Тогда $\exists$ постоянная невырожденная матрица $C$ такая, что $Y_2(t) = Y_1(t) C$.

**Доказательство:**
$\square$ Покажем, что каждая компонента (столбец) $y_j^{(2)}(t)$ матрицы $Y_2(t)$ представима как:
$$y_j^{(2)}(t) = \sum_{i=1}^n c_{ij} y_i^{(1)}(t)$$
Проверим:
$$\frac{d}{dt} y_j^{(2)}(t) = A(t) y_j^{(2)}(t)$$
$$\frac{d}{dt} \left( \sum_{i=1}^n c_{ij} y_i^{(1)}(t) \right) = \sum_{i=1}^n c_{ij} \frac{d}{dt} y_i^{(1)}(t) = \sum_{i=1}^n c_{ij} A(t) y_i^{(1)}(t) = A(t) \left( \sum_{i=1}^n c_{ij} y_i^{(1)}(t) \right)$$
Это верно в силу линейности системы. Таким образом, $Y_2(t) = Y_1(t) C$.

 --- 

photo_2026-05-01 12.41.13 PM.jpeg -- 28

 --- 

### Опр.
Фундаментальная система решений (ФСР) для (3) — это $n$ линейно независимых решений (3) (базис пространства решений).

### Следствие
Пусть $\{y^1(t), \dots, y^n(t)\}$ — ФСР для (3) $\Rightarrow$ общая формула решений (3) имеет вид:
$$y(t) = \sum_{i=1}^n c_i y^i(t), \quad c_1, \dots, c_n \text{ — произв. конст.}$$

### Опр.
Пусть $\{y^1(t), \dots, y^n(t)\}$ — ФСР для (3). Матрицу $Y(t) = \begin{pmatrix} y^1(t) & \vdots & \dots & \vdots & y^n(t) \end{pmatrix}$ называют фундаментальной матрицей решений (ФМР) для (3).

### Следствие
Пусть $Y(t)$ — ФМР для (3) $\Rightarrow$ общая формула решений (3) имеет вид:
$$y(t) = Y(t) \cdot \vec{c}, \quad \vec{c} = \begin{pmatrix} c_1 \\ \vdots \\ c_n \end{pmatrix}$$

### Следствие
Пусть $Y(t)$ — ФМР для (3) $\Rightarrow$ решение задачи Коши $\begin{cases} \frac{dy}{dt} = A(t)y \\ y(t_0) = y_0 \end{cases}$ имеет вид:
$$y(t) = Y(t) Y^{-1}(t_0) y_0$$

### Следствие
Пусть $A(t) \equiv A \Rightarrow e^{tA}$ — ФМР для (3).

### Теорема №5 (о связи ФМР)
Пусть $A(t) \in C(a, b)$ и $Y_1(t), Y_2(t)$ — ФМР для (3) $\Rightarrow \exists B \mid \det B \neq 0$:
$$Y_2(t) = Y_1(t) B$$

### Доказательство
Покажем, что $Y_1^{-1}(t) \cdot Y_2(t) \equiv \text{const} \sim \frac{d}{dt} (Y_1^{-1}(t) \cdot Y_2(t)) = 0 \sim$
$$\sim \left( \frac{d}{dt} Y_1^{-1}(t) \right) Y_2(t) + Y_1^{-1}(t) \frac{d}{dt} Y_2(t) = 0 \quad (*)$$

$$\frac{d}{dt} Y_2(t) = \frac{d}{dt} \begin{pmatrix} y^1(t) & \vdots & \dots & \vdots & y^n(t) \end{pmatrix} = \begin{pmatrix} \frac{dy^1(t)}{dt} & \vdots & \dots & \vdots & \frac{dy^n(t)}{dt} \end{pmatrix} =$$
$$= \begin{pmatrix} A(t)y^1(t) & \vdots & \dots & \vdots & A(t)y^n(t) \end{pmatrix} = A(t) \begin{pmatrix} y^1(t) & \vdots & \dots & \vdots & y^n(t) \end{pmatrix} = A(t) Y_2(t)$$

 --- 

photo_2026-05-01 12.41.15 PM.jpeg -- 29

 --- 

# Линейные однородные системы. Фундаментальная матрица решений.

Аналогично $\frac{d}{dt} \mathcal{Y}_1(t) = A(t) \mathcal{Y}_1(t)$
$$\frac{d}{dt} \mathcal{Y}_1^{-1}(t) = ?$$
$\mathcal{Y}_1(t)$ — невырождена, ибо, если так, возникнет противоречие в одной из прошлых Th
$$\mathcal{Y}_1(t) \cdot \mathcal{Y}_1^{-1}(t) = E$$
$$\left( \frac{d}{dt} \mathcal{Y}_1(t) \right) \mathcal{Y}_1^{-1}(t) + \mathcal{Y}_1(t) \frac{d}{dt} \mathcal{Y}_1^{-1}(t) = 0$$
$$\frac{d}{dt} \mathcal{Y}_1^{-1}(t) = - \mathcal{Y}_1^{-1}(t) \left( \frac{d}{dt} \mathcal{Y}_1(t) \right) \mathcal{Y}_1^{-1}(t) = - \mathcal{Y}_1^{-1}(t) A(t) \mathcal{Y}_1(t) \mathcal{Y}_1^{-1}(t) = - \mathcal{Y}_1^{-1}(t) A(t)$$
Теперь подставим:
$$- \mathcal{Y}_1^{-1}(t) A(t) \mathcal{Y}_2(t) + \mathcal{Y}_1^{-1}(t) A(t) \mathcal{Y}_2(t) = 0$$
$$\Rightarrow \mathcal{Y}_2(t) = \mathcal{Y}_1(t) B$$
$$\det B = \det(\mathcal{Y}_1^{-1}(t) \cdot \mathcal{Y}_2(t)) \neq 0 \quad \blacksquare$$

### Th 6 (об эквивалентном определении ФМР)
Пусть $A(t) \in C(a, b)$. $\mathcal{Y}(t)$ — ФМР для (3) $\Leftrightarrow$ $\mathcal{Y}(t)$ — реш. $\begin{cases} \frac{d \mathcal{Y}}{dt} = A(t) \mathcal{Y} \\ \det \mathcal{Y}(t_0) \neq 0 \end{cases}$

### Доказательство
- $\Rightarrow$:
Пусть $\mathcal{Y}(t)$ — ФМР для (3) $\Rightarrow \frac{d}{dt} \mathcal{Y}(t) = A(t) \mathcal{Y}(t)$ (см. Th 4, 5). Осталось показать, что $\mathcal{Y}(t_0)$ не выр. (очевидно от противного).
- $\Leftarrow$:
Обозначим $i$-й столбец $\mathcal{Y}(t)$ через $y^i(t)$, т.е. $\mathcal{Y}(t) = (y^1(t) \dots y^n(t))$.
Имеем, что $\frac{dy^i}{dt} = A(t) y^i(t)$, т.е. $y^1(t), \dots, y^n(t)$ — реш. (3).
Покажем, что $y^1(t), \dots, y^n(t)$ лин. нез-мы на $(a, b)$:
$$\sum_{i=1}^n c_i y^i(t) = 0 \quad \forall t \in (a, b) \Rightarrow \sum_{i=1}^n c_i y^i(t_0) = 0 \sim$$
$$\sim (y^1(t_0) \dots y^n(t_0)) \begin{pmatrix} c_1 \\ \vdots \\ c_n \end{pmatrix} = \begin{pmatrix} 0 \\ \vdots \\ 0 \end{pmatrix} \sim \mathcal{Y}(t_0) \begin{pmatrix} c_1 \\ \vdots \\ c_n \end{pmatrix} = \begin{pmatrix} 0 \\ \vdots \\ 0 \end{pmatrix}$$
т.к. $\det \mathcal{Y}(t_0) \neq 0$, то $c_1 = \dots = c_n = 0 \Rightarrow$ лин. нез-мы $\Rightarrow$ ФМР. $\blacksquare$

### Следствие
Пусть $\mathcal{Y}(t)$ — ФМР и матрица $B \mid \det B \neq 0 \Rightarrow \mathcal{Y}(t) B$ — ФМР.

### Следствие
Пусть $A(t) \equiv A = T \mathcal{J} T^{-1}$ ($e^{At} = T e^{\mathcal{J}t} T^{-1}$) $\Rightarrow e^{At}$ — ФМР.

### Следствие
$e^{(t-t_0)A}$ — ФМР.

### Доказательство
$$\frac{d \mathcal{Y}}{dt} = A \mathcal{Y}$$
$$\mathcal{Y}(t_0) = e^{(t_0-t_0)A} = e^0 = E \Rightarrow \det \mathcal{Y}(t_0) = \det E = 1 \neq 0 \quad \blacksquare$$

### Опр.
Пусть $\mathcal{Y}(t)$ — реш. матричного ур-ия. $\mathcal{Y}(t)$ наз. **матрицей Вронского**.
ФМР — частный случай матрицы Вронского.

### Th 7 (формула Остроградского-Лиувилля)
Пусть $A(t) \in C(a, b)$, $\mathcal{Y}(t)$ — матрица Вронского.
$$\square: \text{Достаточно показать, что } \frac{d}{dt} W(t) = \operatorname{tr} A(t) W(t)$$
Покажем:
$$\frac{d}{dt} \det \begin{pmatrix} y_{11} & \dots & y_{1n} \\ \vdots & \ddots & \vdots \\ y_{n1} & \dots & y_{nn} \end{pmatrix}$$
т.е. $\frac{dy_1}{dt} = [НРЗБ], \dots, \frac{dy_n}{dt} = [НРЗБ]$
$$\frac{d}{dt} W(t) = \sum_{i=1}^n \det \begin{pmatrix} y_{11} & \dots & y_{1n} \\ \vdots & \ddots & \vdots \\ \frac{d y_{i1}}{dt} & \dots & \frac{d y_{in}}{dt} \\ \vdots & \ddots & \vdots \\ y_{n1} & \dots & y_{nn} \end{pmatrix} = \det \begin{pmatrix} y'_{11} & \dots & y'_{1n} \\ y_{21} & \dots & y_{2n} \\ \vdots & \ddots & \vdots \\ y_{n1} & \dots & y_{nn} \end{pmatrix} + \dots$$

 --- 

photo_2026-05-01 12.41.16 PM.jpeg -- 30

 --- 

### Следствие
$$e^{(t-\tau)A} = e^{tA} \cdot e^{-\tau A}$$

### Доказательство
$\square$: $e^{tA}$ — решение ЗК:
$$\begin{cases} \frac{dy}{dt} = A \cdot y \\ y(0) = E \end{cases}$$

$e^{(t-\tau)A}$ — решение ЗК:
$$\begin{cases} \frac{dy}{dt} = A \cdot y \\ y(\tau) = E \end{cases}$$

$e^{tA}, e^{(t-\tau)A}$ — ФМР для $\frac{dy}{dt} = Ay$
$\Rightarrow \exists B \mid e^{(t-\tau)A} = e^{tA} \cdot B$
При $t = \tau$: $e^{0} = e^{\tau A} \cdot B \Rightarrow E = e^{\tau A} \cdot B \Rightarrow B = e^{-\tau A}$. $\square$

### Опр.
Пусть $y^1(t), \dots, y^n(t)$ — реш (3). Тогда матрица $(y^1(t) \vdots \dots \vdots y^n(t))$ называется матрицей Вронского, а $W(t) = \det(y^1(t) \vdots \dots \vdots y^n(t))$ — определитель Вронского (вронскиан).

### Замечание
ФМР — частный случай матрицы Вронского.

### Th 7 (Формула Остроградского–Лиувилля)
Пусть $A(t) \in C(a, b) \Rightarrow W(t) = e^{\int_{t_0}^t \operatorname{tr} A(s) \, ds} W(t_0)$.

### Доказательство
$\square$: Достаточно показать $W(t)$ — реш $\frac{dw}{dt} = \operatorname{tr} A(t) w$.
Положим при $n = 2$:
$$\frac{d}{dt} W(t) = \frac{d}{dt} \det \begin{pmatrix} y_1^1(t) & y_1^2(t) \\ y_2^1(t) & y_2^2(t) \end{pmatrix}$$
$y^1(t) = \begin{pmatrix} y_1^1(t) \\ y_2^1(t) \end{pmatrix}, y^2(t) = \begin{pmatrix} y_1^2(t) \\ y_2^2(t) \end{pmatrix}$ — реш (3).

Т.е.
$$\begin{cases} \frac{dy_1^1}{dt} = a_{11}(t)y_1^1 + a_{12}(t)y_2^1 \\ \frac{dy_2^1}{dt} = a_{21}(t)y_1^1 + a_{22}(t)y_2^1 \end{cases} \quad \begin{cases} \frac{dy_1^2}{dt} = a_{11}(t)y_1^2 + a_{12}(t)y_2^2 \\ \frac{dy_2^2}{dt} = a_{21}(t)y_1^2 + a_{22}(t)y_2^2 \end{cases}$$

$$\frac{d}{dt} W(t) = \frac{d}{dt} \det \begin{pmatrix} y_1^1 & y_1^2 \\ y_2^1 & y_2^2 \end{pmatrix} = \det \begin{pmatrix} \frac{dy_1^1}{dt} & \frac{dy_1^2}{dt} \\ y_2^1 & y_2^2 \end{pmatrix} + \det \begin{pmatrix} y_1^1 & y_1^2 \\ \frac{dy_2^1}{dt} & \frac{dy_2^2}{dt} \end{pmatrix} =$$
$$= \det \begin{pmatrix} a_{11} y_1^1 + a_{12} y_2^1 & a_{11} y_1^2 + a_{12} y_2^2 \\ y_2^1 & y_2^2 \end{pmatrix} + \det \begin{pmatrix} y_1^1 & y_1^2 \\ a_{21} y_1^1 + a_{22} y_2^1 & a_{21} y_1^2 + a_{22} y_2^2 \end{pmatrix} =$$
$$= \det \begin{pmatrix} a_{11} y_1^1 & a_{11} y_1^2 \\ y_2^1 & y_2^2 \end{pmatrix} + \det \begin{pmatrix} y_1^1 & y_1^2 \\ a_{22} y_2^1 & a_{22} y_2^2 \end{pmatrix} =$$
$$= a_{11} W + a_{22} W = (a_{11} + a_{22}) W = \operatorname{tr} A \cdot W$$
$\frac{dw}{dt} = \operatorname{tr} A \cdot w$. $\square$

 --- 

photo_2026-05-01 12.41.17 PM.jpeg -- 31

 --- 

# 20.11.25 лекция. § Линейные неоднородные системы д. у.

$$ \frac{dy}{dt} = A(t)y + h(t) \quad (1) $$

$$ y(t) = \begin{pmatrix} y_1(t) \\ \vdots \\ y_n(t) \end{pmatrix}; A(t) = \begin{pmatrix} a_{11}(t) & \dots & a_{1n}(t) \\ \vdots & \ddots & \vdots \\ a_{n1}(t) & \dots & a_{nn}(t) \end{pmatrix}; h(t) = \begin{pmatrix} h_1(t) \\ \vdots \\ h_n(t) \end{pmatrix} $$

### Тн 1
Пусть $A(t), h(t) \in C(a, b)$ и $Y(t)$ — ФСР для системы $\frac{dy}{dt} = A(t)y \quad (3)$.
Тогда решение ЗК (2) имеет вид:
$$ y(t) = Y(t) Y^{-1}(t_0) y_0 + \int_{t_0}^t Y(t) Y^{-1}(s) h(s) \, ds $$
Где (2):
$$ \begin{cases} \frac{dy}{dt} = A(t)y + h(t) \\ y(t_0) = y_0 \end{cases} $$

### Доказательство
Докажем, используя метод вариации произвольной постоянной. Общее решение лин. одн. системы (3) имеет вид:
$$ y_{одн}(t) = Y(t) \cdot \vec{c}, \quad \vec{c} = \begin{pmatrix} c_1 \\ \vdots \\ c_n \end{pmatrix} $$
Ищем решение ЗК (2) в след. виде:
$$ y(t) = Y(t) u(t), \quad u(t) = \begin{pmatrix} u_1(t) \\ \vdots \\ u_n(t) \end{pmatrix} $$
$$ \frac{dy}{dt} = \frac{dY}{dt} u + Y \frac{du}{dt} = AY u + h $$
Так как $\frac{dY}{dt} = AY$, то:
$$ \implies \begin{cases} Y(t) \frac{du}{dt} = h(t) \\ u(t_0) = Y^{-1}(t_0) y_0 \end{cases} \iff \begin{cases} \frac{du}{dt} = Y^{-1}(t) h(t) \mid \int_{t_0}^t \\ u(t_0) = Y^{-1}(t_0) y_0 \end{cases} $$
$$ \iff u(t) = Y^{-1}(t_0) y_0 + \int_{t_0}^t Y^{-1}(s) h(s) \, ds $$
$$ y(t) = Y(t) u(t) \quad \blacksquare $$

### Следствие 1
Пусть $A(t), h(t) \in C(a, b)$ и $Y(t)$ — ФСР для (3) $\implies$ общая формула реш. для (1) имеет вид:
$$ y(t) = Y(t)\vec{c} + \int_{t_0}^t Y(t) Y^{-1}(s) h(s) \, ds $$

### Следствие 2
$$ y_{он} = y_{оо} + y_{чн} $$
- $y_{он}$ — общая формула реш. (1)
- $y_{оо}$ — общая формула реш. (3)
- $y_{чн}$ — частное реш. (1)

### Следствие 3
Пусть $A(t) \equiv A$, [НРЗБ]
$$ y(t) = e^{A(t-t_0)} y_0 + \int_{t_0}^t e^{A(t-s)} h(s) \, ds $$

### Лемма (Гронуолла–Беллмана)
Пусть $u(t), L(t) \in C[t_0, T]$
$$ u(t) \le u_0 + \int_{t_0}^t L(s) u(s) \, ds $$
Тогда 
$$ u(t) \le u_0 e^{\int_{t_0}^t L(s) \, ds} $$

### Доказательство
Введём $v(t) = u_0 + \int_{t_0}^t L(s) u(s) \, ds$.
Имеем $u(t) \le v(t)$.
$$ \frac{dv}{dt} = L(t) u(t) \le L(t) v(t) $$
$$ \frac{dv}{dt} - L(t) v(t) \le 0 \mid \cdot e^{-\int_{t_0}^t L(s) \, ds} $$
$$ \frac{d}{dt} \left( e^{-\int_{t_0}^t L(s) \, ds} v(t) \right) \le 0 $$
$$ e^{-\int_{t_0}^t L(s) \, ds} v(t) \le v(t_0) = u_0 $$
$$ u(t) \le v(t) \le u_0 e^{\int_{t_0}^t L(s) \, ds} \quad \blacksquare $$

### Следствие
Пусть $A(t) \in C(a, b)$, $y(t)$ — реш. (3), $y(t_0) = y_0$.
$$ \|y(t)\| \le \|y_0\| e^{\int_{t_0}^t \|A(s)\| \, ds} $$
Доказательство: $y(t)$ — реш., $y(t) = y_0 + \int_{t_0}^t A(s) y(s) \, ds$.
$$ \|y(t)\| \le \|y_0\| + \int_{t_0}^t \|A(s)\| \|y(s)\| \, ds $$
Желаемое [НРЗБ: следует из леммы Гронуолла].

 --- 

photo_2026-05-01 12.41.18 PM.jpeg -- 32

 --- 

### Следствие 3
Пусть $A(t) \equiv A, h(t) \in C(a, b) \Rightarrow$ реш. ЗК (2) имеет вид:
$$y(t) = e^{(t-t_0)A} y_0 + \int_{t_0}^t e^{(t-s)A} h(s) ds$$

### Лемма (Гронуолла)
Пусть $u(t), L(t), \varphi(t) \in C(a, b)$, при этом $0 \le L(t), 0 \le u(t), 0 \le \varphi(t)$,
$u(t) \le u_0 + \int_{t_0}^t (L(s)u(s) + \varphi(s)) ds, \quad t > t_0$.
Тогда $u(t) \le e^{\int_{t_0}^t L(s) ds} u_0 + \int_{t_0}^t e^{\int_s^t L(\tau) d\tau} \varphi(s) ds, \quad t > t_0$.

### Доказательство
$\square$: Введём обозначение $v(t) = u_0 + \int_{t_0}^t (L(s)u(s) + \varphi(s)) ds$
Имеем $u(t) \le v(t), v(t_0) = u_0$
$$\frac{dv}{dt} = L(t) u(t) + \varphi(t) \le L(t) v(t) + \varphi(t)$$
$$\frac{dv}{dt} - L(t) v(t) \le \varphi(t) \quad \mid \cdot e^{-\int_{t_0}^t L(s) ds}$$
$$\frac{d}{dt} \left( e^{-\int_{t_0}^t L(s) ds} v(t) \right) \le \varphi(t) e^{-\int_{t_0}^t L(s) ds} \quad \mid \int_{t_0}^t$$
$$e^{-\int_{t_0}^t L(s) ds} v(t) - u_0 \le \int_{t_0}^t e^{-\int_{t_0}^s L(\tau) d\tau} \varphi(s) ds$$
$$u(t) \le v(t) \le e^{\int_{t_0}^t L(s) ds} u_0 + \int_{t_0}^t e^{\int_s^t L(\tau) d\tau} \varphi(s) ds \blacksquare$$

### Следствие
Пусть $A(t), h(t) \in C(a, b) \Rightarrow$ для решения $y(t)$ ЗК (2) справедлива оценка
$$\|y(t)\| \le e^{\int_{t_0}^t \|A(s)\| ds} \|y_0\| + \int_{t_0}^t e^{\int_s^t \|A(\tau)\| d\tau} \|h(s)\| ds$$

### Доказательство
$\square$: $y(t)$ — реш.;
$$y(t) = y_0 + \int_{t_0}^t (A(s)y(s) + h(s)) ds$$
$$\|y(t)\| \le \|y_0\| + \int_{t_0}^t (\|A(s)\| \cdot \|y(s)\| + \|h(s)\|) ds$$
и из леммы Гронуолла получим желаемое $\blacksquare$

 --- 

photo_2026-05-01 12.41.24 PM.jpeg -- 33

 --- 

# Лекция: Линейные системы и зависимость решений от параметров

### Th 2
Пусть $A(t), h(t), \tilde{h}(t) \in C(a, b)$; $y(t)$ — реш. (2); $\tilde{y}(t)$ — реш.
$$ \frac{d \tilde{y}}{d t} = A(t) \tilde{y}(t) + \tilde{h}(t) $$
$$ \tilde{y}(t_0) = \tilde{y}_0 $$
Тогда:
$$ \| \tilde{y}(t) - y(t) \| \le e^{\left| \int_{t_0}^t \| A(s) \| ds \right|} \| \tilde{y}_0 - y_0 \| + \left| \int_{t_0}^t e^{\left| \int_{s}^t \| A(\tau) \| d\tau \right|} \| \tilde{h}(s) - h(s) \| ds \right| $$

### Доказательство
$\square$: Достаточно заметить, что $z(t) = \tilde{y}(t) - y(t)$ — реш.
$$ \begin{cases} \frac{d z}{d t} = A(t)z + \tilde{h}(t) - h(t) \\ z(t_0) = \tilde{y}_0 - y_0 \end{cases} $$
и воспользоваться следствием. $\blacksquare$

### Th 3
Пусть $A(t), \tilde{A}(t), h(t), \tilde{h}(t) \in C(a, b)$; $y(t)$ — решение (2); $\tilde{y}(t)$ — реш.
$$ \begin{cases} \frac{d \tilde{y}}{d t} = \tilde{A}(t)\tilde{y}(t) + \tilde{h}(t) \\ \tilde{y}(t_0) = \tilde{y}_0 \end{cases} $$
Выберем $[\alpha, \beta] \subset (a, b) \mid t_0 \in [\alpha, \beta] \Rightarrow \forall \varepsilon > 0 \exists \delta > 0$: $\forall \tilde{A}(t), \tilde{h}(t), \tilde{y}_0$
$$ \max_{t \in [\alpha, \beta]} \| \tilde{A}(s) - A(s) \| + \max_{t \in [\alpha, \beta]} \| \tilde{h}(s) - h(s) \| + \| \tilde{y}_0 - y_0 \| < \delta $$
Тогда $\| \tilde{y}(t) - y(t) \| < \varepsilon \quad \forall t \in [\alpha, \beta]$

### Доказательство
$\square$:
$$ \frac{d}{dt} (\tilde{y}(t) - y(t)) = \tilde{A}(t)\tilde{y}(t) - A(t)y(t) + \tilde{h}(t) - h(t) \pm \tilde{A}(t)y(t) $$
$$ \begin{cases} \frac{d}{dt}(\tilde{y}(t) - y(t)) = \tilde{A}(t)(\tilde{y}(t) - y(t)) + \underbrace{(\tilde{A}(t) - A(t))y(t) + \tilde{h}(t) - h(t)}_{F(t)} \\ (\tilde{y} - y)|_{t=t_0} = \tilde{y}_0 - y_0 \end{cases} $$
Используя следствие после леммы, получим:
$$ \| \tilde{y}(t) - y(t) \| \le e^{\left| \int_{t_0}^t \| \tilde{A}(s) \| ds \right|} \| \tilde{y}_0 - y_0 \| + \left| \int_{t_0}^t e^{\left| \int_{s}^t \| \tilde{A}(\tau) \| d\tau \right|} \| F(s) \| ds \right| $$
Пусть $q = \max_{[\alpha, \beta]} \| y(s) \|$ и $p = \max_{[\alpha, \beta]} \| A(s) \|$
$$ \| \tilde{A}(t) \| \le \| A(t) \| + \| \tilde{A}(t) - A(t) \| \le p + \max_{[\alpha, \beta]} \| \tilde{A}(s) - A(s) \| $$
[НРЗБ: продолжение оценки]
$$ \int_{t_0}^t \| \tilde{A}(s) \| ds \le [НРЗБ] $$
$$ \| \tilde{y}(t) - y(t) \| \le \dots + \max_{[\alpha, \beta]} \| \tilde{h}(s) - h(s) \| \dots $$

### Пример 1
$$ \frac{dy}{dt} = \begin{pmatrix} 1 & 1 \\ 0 & 1+\varepsilon \end{pmatrix} y $$
$\varepsilon \neq 0$
$$ J = \begin{pmatrix} 1 & 0 \\ 0 & 1+\varepsilon \end{pmatrix} $$
$$ T e^{tJ} = \begin{pmatrix} [НРЗБ] \end{pmatrix} $$
Предположение: [НРЗБ]

# Лекция (27.11.25)
$A - n \times n$
$\psi(t, \sigma)$ — [НРЗБ: матрицант/ФСР]
$\psi(t, t_1, t_2) = [НРЗБ]$
$\psi(t, \tau, \dots)$

### Лемма 1
$$ e^{At} = \psi(t, 0) $$
$\square$: (1) $\frac{d}{dt} [НРЗБ]$

 --- 

photo_2026-05-01 12.41.25 PM.jpeg -- 34

 --- 

$$\int_{t_0}^t \|\tilde{A}(s)\| \, ds \le (\beta - \alpha) \left( p + \max_{[\alpha, \beta]} \|\tilde{A}(s) - A(s)\| \right)$$

$$\|\tilde{y}(t) - y(t)\| \le e^{(\beta - \alpha) \left( p + \max\limits_{[\alpha, \beta]} \|\tilde{A}(s) - A(s)\| \right)} \left( \|\tilde{y}_0 - y_0\| + (\beta - \alpha) \left( q \max_{[\alpha, \beta]} \|\tilde{A}(s) - A(s)\| + \max_{[\alpha, \beta]} \|\tilde{h}(s) - h(s)\| \right) \right) \blacksquare$$

## § 3 ФСР для линейных однородных систем с постоянными коэффициентами

$$\frac{dy}{dt} = Ay; \quad A = T J T^{-1}; \quad T e^{tJ} - \text{ФМР}$$

### Пример 1
$$\frac{dy}{dt} = \begin{pmatrix} 1 & 1 \\ 0 & 1+\epsilon \end{pmatrix} y$$
$\epsilon \neq 0$
$$J = \begin{pmatrix} 1 & 0 \\ 0 & 1+\epsilon \end{pmatrix}; \quad T = \begin{pmatrix} 1 & \frac{1}{\epsilon} \\ 0 & 1 \end{pmatrix}; \quad e^{tJ} = \begin{pmatrix} e^t & 0 \\ 0 & e^{(1+\epsilon)t} \end{pmatrix}$$
$$T e^{tJ} = \begin{pmatrix} 1 & \frac{1}{\epsilon} \\ 0 & 1 \end{pmatrix} \begin{pmatrix} e^t & 0 \\ 0 & e^{(1+\epsilon)t} \end{pmatrix} = \begin{pmatrix} e^t & \frac{e^{(1+\epsilon)t} - e^t}{\epsilon} \\ 0 & e^{(1+\epsilon)t} \end{pmatrix} \xrightarrow{\epsilon \to 0} \begin{pmatrix} e^t & t e^t \\ 0 & e^t \end{pmatrix}$$
(справа)

**Предложение** $(\star)$

# 27.11.25 лекция Демиденко
$A - n \times n \quad \tilde{\lambda}_1, \tilde{\lambda}_2, \dots, \tilde{\lambda}_n \mid \tilde{\lambda}_j \neq \tilde{\lambda}_k$
$$\psi(t, \tilde{\lambda}_1) = e^{\tilde{\lambda}_1 t}$$
$$\psi(t, \tilde{\lambda}_1, \tilde{\lambda}_2) = \frac{\psi(t, \tilde{\lambda}_2) - \psi(t, \tilde{\lambda}_1)}{\tilde{\lambda}_2 - \tilde{\lambda}_1} = \frac{e^{\tilde{\lambda}_2 t} - e^{\tilde{\lambda}_1 t}}{\tilde{\lambda}_2 - \tilde{\lambda}_1}$$
$$\psi(t, \tilde{\lambda}_1, \tilde{\lambda}_2, \tilde{\lambda}_3) = \frac{\psi(t, \tilde{\lambda}_2, \tilde{\lambda}_3) - \psi(t, \tilde{\lambda}_1, \tilde{\lambda}_2)}{\tilde{\lambda}_3 - \tilde{\lambda}_1}$$
$$\psi(t, \tilde{\lambda}_1, \dots, \tilde{\lambda}_k) = \frac{\psi(t, \tilde{\lambda}_2, \dots, \tilde{\lambda}_k) - \psi(t, \tilde{\lambda}_1, \dots, \tilde{\lambda}_{k-1})}{\tilde{\lambda}_k - \tilde{\lambda}_1}$$

### Лемма 1
$$e^{tJ} = \psi(t, \tilde{\lambda}_1) E + \psi(t, \tilde{\lambda}_1, \tilde{\lambda}_2) (J - \tilde{\lambda}_1 E) + \dots + \psi(t, \tilde{\lambda}_1, \dots, \tilde{\lambda}_n) (J - \tilde{\lambda}_1 E) \dots (J - \tilde{\lambda}_{n-1} E)$$

### Доказательство
- 1) $\frac{d}{dt} Y(t) = J Y(t), \quad Y(0) = E; \quad (J - \tilde{\lambda}_1 E) \dots (J - \tilde{\lambda}_n E) = 0$

 --- 

photo_2026-05-01 12.41.26 PM.jpeg -- 35

 --- 

# (I)

$$ e^{tJ} = \begin{pmatrix} e^{\tilde{\lambda}_1 t} & [НРЗБ] \\ \mathbb{0} & \ddots & \\ & & e^{\tilde{\lambda}_n t} \end{pmatrix} $$

Рассмотрим при $n=2$:
$$ e^{tJ} = \begin{pmatrix} e^{\tilde{\lambda}_1 t} & [НРЗБ] \\ 0 & e^{\tilde{\lambda}_2 t} \end{pmatrix} = \begin{pmatrix} \psi(t, \tilde{\lambda}_1) & 0 \\ 0 & \psi(t, \tilde{\lambda}_1) \end{pmatrix} + \begin{pmatrix} 0 & \psi(t, \tilde{\lambda}_1, \tilde{\lambda}_2) \cdot 1 \\ 0 & (\tilde{\lambda}_2 - \tilde{\lambda}_1) \psi(t, \tilde{\lambda}_1, \tilde{\lambda}_2) \end{pmatrix} = $$
$$ = \psi(t, \tilde{\lambda}_1) E + \dots $$

## Th 1
$$ e^{tA} = \psi(t, \tilde{\lambda}_1) E + \psi(t, \tilde{\lambda}_1, \tilde{\lambda}_2) (A - \tilde{\lambda}_1 E) + \dots + \psi(t, \tilde{\lambda}_1, \dots, \tilde{\lambda}_n) (A - \tilde{\lambda}_1 E) \dots (A - \tilde{\lambda}_{n-1} E) $$

### Доказательство:
$T^{-1} A T = J$ в ЖНФ
$$ e^{tA} = T e^{tJ} T^{-1} = T \left( \psi(t, \tilde{\lambda}_1) E + \psi(t, \tilde{\lambda}_1, \tilde{\lambda}_2) (J - \tilde{\lambda}_1 E) + \dots + \psi(t, \tilde{\lambda}_1, \dots, \tilde{\lambda}_n) (J - \tilde{\lambda}_1 E) \dots (J - \tilde{\lambda}_{n-1} E) \right) T^{-1} = $$
$$ = \psi(t, \tilde{\lambda}_1) E + \psi(t, \tilde{\lambda}_1, \tilde{\lambda}_2) T (J - \tilde{\lambda}_1 E) T^{-1} + \dots + \psi(t, \tilde{\lambda}_1, \dots, \tilde{\lambda}_n) T (J - \tilde{\lambda}_1 E) \dots (J - \tilde{\lambda}_{n-1} E) T^{-1} = $$
$$ = \psi(t, \tilde{\lambda}_1) E + \psi(t, \tilde{\lambda}_1, \tilde{\lambda}_2) (A - \tilde{\lambda}_1 E) + \dots + \psi(t, \tilde{\lambda}_1, \dots, \tilde{\lambda}_n) T (J - \tilde{\lambda}_1 E) T^{-1} T (J - \tilde{\lambda}_2 E) T^{-1} \dots T (J - \tilde{\lambda}_{n-1} E) T^{-1} = $$
$$ = \psi(t, \tilde{\lambda}_1) E + \psi(t, \tilde{\lambda}_1, \tilde{\lambda}_2) (A - \tilde{\lambda}_1 E) + \dots + \psi(t, \tilde{\lambda}_1, \dots, \tilde{\lambda}_n) (A - \tilde{\lambda}_1 E) \dots (A - \tilde{\lambda}_{n-1} E) $$
$\square$

### Лемма:
$\Psi(t) = \begin{pmatrix} \psi(t, \tilde{\lambda}_1) \\ \psi(t, \tilde{\lambda}_1, \tilde{\lambda}_2) \\ \vdots \\ \psi(t, \tilde{\lambda}_1, \dots, \tilde{\lambda}_n) \end{pmatrix}$ — решение $\frac{d}{dt} \Psi = \begin{pmatrix} \tilde{\lambda}_1 & 0 & \dots & 0 \\ 1 & \tilde{\lambda}_2 & \dots & 0 \\ \vdots & \ddots & \ddots & \vdots \\ 0 & \dots & 1 & \tilde{\lambda}_n \end{pmatrix} \Psi$
$\Psi|_{t=0} = \begin{pmatrix} 1 \\ 0 \\ \vdots \\ 0 \end{pmatrix}$

### Доказательство:
$$ \frac{d}{dt} \psi(t, \tilde{\lambda}_1) = \tilde{\lambda}_1 e^{\tilde{\lambda}_1 t} = \tilde{\lambda}_1 \psi(t, \tilde{\lambda}_1) $$
$$ \frac{d}{dt} \psi(t, \tilde{\lambda}_1, \tilde{\lambda}_2) \equiv \frac{1}{\tilde{\lambda}_2 - \tilde{\lambda}_1} \left( \tilde{\lambda}_2 e^{\tilde{\lambda}_2 t} - \tilde{\lambda}_1 e^{\tilde{\lambda}_1 t} \right) = \frac{1}{\tilde{\lambda}_2 - \tilde{\lambda}_1} \left( \tilde{\lambda}_2 \psi(t, \tilde{\lambda}_2) - \tilde{\lambda}_1 \psi(t, \tilde{\lambda}_1) \right) = $$
$$ = \frac{1}{\tilde{\lambda}_2 - \tilde{\lambda}_1} \left( \tilde{\lambda}_2 \psi(t, \tilde{\lambda}_2) - \tilde{\lambda}_2 \psi(t, \tilde{\lambda}_1) + \tilde{\lambda}_2 \psi(t, \tilde{\lambda}_1) - \tilde{\lambda}_1 \psi(t, \tilde{\lambda}_1) \right) = $$
$$ = \frac{\tilde{\lambda}_2 (\psi(t, \tilde{\lambda}_2) - \psi(t, \tilde{\lambda}_1))}{\tilde{\lambda}_2 - \tilde{\lambda}_1} + \frac{(\tilde{\lambda}_2 - \tilde{\lambda}_1) \psi(t, \tilde{\lambda}_1)}{\tilde{\lambda}_2 - \tilde{\lambda}_1} = \tilde{\lambda}_2 \psi(t, \tilde{\lambda}_1, \tilde{\lambda}_2) + \psi(t, \tilde{\lambda}_1) $$
Последовательно, снизу вверх действуем и приравниваем.
$\square$

---
(Правая страница)

Можем считать, что $\tilde{\lambda}_i$ будут различными.

### Th 2
[НРЗБ]

# 04.12.23
$$ \frac{dy}{dt} = Ay $$
$\{ \tilde{\lambda}_1, \dots, \tilde{\lambda}_n \}$
$\psi(t, \tilde{\lambda}_1)$
$\psi(t, \tilde{\lambda}_1, \tilde{\lambda}_2)$
$\dots$
$$ e^{tA} = \psi(t, \tilde{\lambda}_1) E + (A - \tilde{\lambda}_1 E) \psi(t, \tilde{\lambda}_1, \tilde{\lambda}_2) + \dots $$
$\square$

### Th 3 (оценка нормы матричной экспоненты)
Пусть $\tilde{\lambda}_i$ [НРЗБ]
$$ \| e^{tA} \| \le [НРЗБ] $$

### Доказательство:
$\psi(t, \tilde{\lambda}_1, \dots, \tilde{\lambda}_k)$
База $k=1$
[НРЗБ]

 --- 

photo_2026-05-01 12.41.27 PM.jpeg -- 36

 --- 

Можем так $\|A_\epsilon - A\| \xrightarrow{\epsilon \to 0} 0$. Тогда можем чуть сдвинуть так, что собс. числа будут различны.

## Теорема 2
to be continued...

$$ \frac{d}{dt} \psi(t; \tilde{\lambda}_1, \dots, \tilde{\lambda}_n) = \tilde{\lambda}_n \psi(t; \tilde{\lambda}_1, \dots, \tilde{\lambda}_n) + \psi(t; \tilde{\lambda}_1, \dots, \tilde{\lambda}_{n-1}) $$
$$ \vdots $$
$$ \frac{d}{dt} \psi(t; \tilde{\lambda}_1, \tilde{\lambda}_2) = \tilde{\lambda}_2 \psi(t; \tilde{\lambda}_1, \tilde{\lambda}_2) + \psi(t; \tilde{\lambda}_1) $$
$$ \frac{d}{dt} \psi(t; \tilde{\lambda}_1) = \tilde{\lambda}_1 \psi(t; \tilde{\lambda}_1) $$
$$ \psi(t; \tilde{\lambda}_1) \equiv e^{\tilde{\lambda}_1 t} $$
$$ \psi(t; \tilde{\lambda}_1, \tilde{\lambda}_2) = \int_0^t e^{\tilde{\lambda}_2(t-s)} \psi(s; \tilde{\lambda}_1) \, ds $$
$$ \psi(t; \tilde{\lambda}_1, \dots, \tilde{\lambda}_j) = \int_0^t e^{\tilde{\lambda}_j(t-s)} \psi(s; \tilde{\lambda}_1, \dots, \tilde{\lambda}_{j-1}) \, ds $$

# Лекция (04. 12. 25)

$$ \frac{dy}{dt} = Ay $$
$$ \{ \tilde{\lambda}_1, \dots, \tilde{\lambda}_n \} = \operatorname{Sp} A $$
$$ \psi(t, \tilde{\lambda}_1) = e^{\tilde{\lambda}_1 t} $$
$$ \psi(t, \tilde{\lambda}_1, \tilde{\lambda}_2) = \int_0^t e^{\tilde{\lambda}_2(t-s)} \psi(s, \tilde{\lambda}_1) \, ds $$
$$ \psi(t, \tilde{\lambda}_1, \dots, \tilde{\lambda}_k, \tilde{\lambda}_{k+1}) = \int_0^t e^{\tilde{\lambda}_{k+1}(t-s)} \psi(s, \tilde{\lambda}_1, \dots, \tilde{\lambda}_k) \, ds $$
$$ e^{tA} = \psi(t, \tilde{\lambda}_1) E + \psi(t, \tilde{\lambda}_1, \tilde{\lambda}_2)(A - \tilde{\lambda}_1 E) + \dots + \psi(t, \tilde{\lambda}_1, \dots, \tilde{\lambda}_n)(A - \tilde{\lambda}_1 E) \dots (A - \tilde{\lambda}_{n-1} E) $$

### Теорема 3 (оценка Гельфанда-Шилова)

Пусть $\tilde{\lambda}_1, \dots, \tilde{\lambda}_n$ — собственные значения $A$ и $S \mid \operatorname{Re} \tilde{\lambda}_i \le S, i = 1, \dots, n \implies$
$$ \implies \| e^{tA} \| \le e^{St} \left( 1 + \frac{2\|A\|t}{1!} + \frac{(2\|A\|t)^2}{2!} + \dots + \frac{(2\|A\|t)^{n-1}}{(n-1)!} \right), t \ge 0 $$

### Доказательство:

- $|\psi(t, \tilde{\lambda}_1, \dots, \tilde{\lambda}_k)| \le e^{St} \frac{t^{k-1}}{(k-1)!}, k = 1, \dots, n$
- База: $|\psi(t, \tilde{\lambda}_1)| = |e^{\tilde{\lambda}_1 t}| = |e^{\operatorname{Re} \tilde{\lambda}_1 t + i \operatorname{Im} \tilde{\lambda}_1 t}| = |e^{\operatorname{Re} \tilde{\lambda}_1 t}| \cdot |e^{i \operatorname{Im} \tilde{\lambda}_1 t}| = e^{\operatorname{Re} \tilde{\lambda}_1 t} \le e^{St}$

 --- 

photo_2026-05-01 12.41.28 PM.jpeg -- 37

 --- 

# Оценка нормы матричной экспоненты и линейные уравнения высших порядков

Предположим, что $|\psi(t, \tilde{\lambda}_1, \dots, \tilde{\lambda}_k)| \le e^{\delta t} \frac{t^{k-1}}{(k-1)!}$

Тогда:
$$|\psi(t, \tilde{\lambda}_1, \dots, \tilde{\lambda}_k, \tilde{\lambda}_{k+1})| = \left| \int_0^t e^{\tilde{\lambda}_{k+1}(t-s)} \psi(s, \tilde{\lambda}_1, \dots, \tilde{\lambda}_k) \, ds \right| \le$$
$$\le \int_0^t |e^{\tilde{\lambda}_{k+1}(t-s)}| \cdot |\psi(s, \tilde{\lambda}_1, \dots, \tilde{\lambda}_k)| \, ds \le$$
$$\le \int_0^t e^{\delta(t-s)} e^{\delta s} \frac{s^{k-1}}{(k-1)!} \, ds = e^{\delta t} \int_0^t \frac{s^{k-1}}{(k-1)!} \, ds = e^{\delta t} \frac{t^k}{k!}$$

Покажем, что $|\tilde{\lambda}_k| \le \|A\|$
$$A \vec{v}_k = \tilde{\lambda}_k \vec{v}_k$$
$$\|\tilde{\lambda}_k \vec{v}_k\| = |\tilde{\lambda}_k| \cdot \|\vec{v}_k\| = \|A \vec{v}_k\| \le \|A\| \cdot \|\vec{v}_k\|$$

$$\|e^{tA}\| \le |\psi(t, \tilde{\lambda}_1)| + |\psi(t, \tilde{\lambda}_1, \tilde{\lambda}_2)| \|A - \tilde{\lambda}_1 E\| + \dots + |\psi(t, \tilde{\lambda}_1, \dots, \tilde{\lambda}_n)| \cdot \|A - \tilde{\lambda}_1 E\| \dots \|A - \tilde{\lambda}_{n-1} E\|$$

$$\|A - \tilde{\lambda}_n E\| \le \|A\| + |\tilde{\lambda}_n| \le 2\|A\|$$

### Тн 4
$$e^{-|t| \|A\|} \le \|e^{tA}\| \le e^{|t| \|A\|}$$

### Доказательство
1) $\|e^{tA}\| = \|E + tA + \frac{t^2 A^2}{2} + \dots\| \le 1 + |t| \|A\| + \frac{|t|^2 \|A\|^2}{2} + \dots = e^{|t| \|A\|}$
2) $1 = \|E\| = \|e^{tA} \cdot e^{-tA}\| \le \|e^{tA}\| \cdot \|e^{-tA}\| \le \|e^{tA}\| \cdot e^{|-t| \|A\|} = \|e^{tA}\| e^{|t| \|A\|} \blacksquare$

---

$$\frac{d^n u}{dt^n} + a_1 \frac{d^{n-1} u}{dt^{n-1}} + \dots + a_n u = 0 \quad (\Delta)$$

$$y(t) = \begin{pmatrix} y_1(t) \\ \vdots \\ y_n(t) \end{pmatrix} = \begin{pmatrix} u(t) \\ \vdots \\ u^{(n-1)}(t) \end{pmatrix}$$

$$\frac{dy}{dt} = \begin{pmatrix} u'(t) \\ \vdots \\ u^{(n)}(t) \end{pmatrix} = \begin{pmatrix} y_2(t) \\ \vdots \\ y_n(t) \\ -a_n y_1 - \dots - a_1 y_n \end{pmatrix}$$

$$\frac{dy}{dt} = Ay$$

$$A = \begin{pmatrix} 0 & 1 & & \mathbb{O} \\ \vdots & 0 & \ddots & \\ \mathbb{O} & & \ddots & 1 \\ -a_n & -a_{n-1} & \dots & -a_1 \end{pmatrix}$$

 --- 

photo_2026-05-01 12.41.29 PM.jpeg -- 38

 --- 

### Теорема 5

Множество решений уравнения $(\Delta)$ образует линейное пространство размерности $n$.

### Опр.
**Фунд. сист. решений (ФСР)** для $(\Delta)$ — базис пространства решений.

$$P_n\left(\frac{d}{dt}\right) = \frac{d^n}{dt^n} + a_1 \frac{d^{n-1}}{dt^{n-1}} + \dots + a_n E$$
$$(\Delta) \sim P_n\left(\frac{d}{dt}\right) u = 0$$
$P_n(\lambda) = \lambda^n + a_1 \lambda^{n-1} + \dots + a_n$ — **хар. полином**, $P_n(\lambda) = 0$ — **хар. ур-е**.
$\lambda_1, \dots, \lambda_n$ — корни $P_n(\lambda) = 0$.
$P_n(\lambda) = (\lambda - \lambda_1) \dots (\lambda - \lambda_n)$

### Лемма
Пусть $\lambda_1, \dots, \lambda_n$ — корни $P_n(\lambda) \Rightarrow P_n\left(\frac{d}{dt}\right) = \left(\frac{d}{dt} - \lambda_1 E\right) \dots \left(\frac{d}{dt} - \lambda_n E\right)$

### Доказательство
$\square: n=2$
$$P_2(\lambda) = \lambda^2 + a_1 \lambda + a_2 = (\lambda - \lambda_1)(\lambda - \lambda_2)$$
$a_1 = -\lambda_1 - \lambda_2$; $a_2 = \lambda_1 \lambda_2$
$$\left(\frac{d}{dt} - \lambda_1 E\right) \left(\frac{d}{dt} - \lambda_2 E\right) u = \left(\frac{d}{dt} - \lambda_1 E\right) \left(\frac{du}{dt} - \lambda_2 u\right) = \frac{d^2u}{dt^2} - \lambda_2 \frac{du}{dt} - \lambda_1 \frac{du}{dt} + \lambda_1 \lambda_2 u = \frac{d^2u}{dt^2} + a_1 \frac{du}{dt} + a_2 u = P_2\left(\frac{d}{dt}\right) u$$
$\blacksquare$

### Следствие
Пусть $\lambda_1, \dots, \lambda_n$ — корни $P_n(\lambda)$ и $\{\lambda_{j_1}, \dots, \lambda_{j_n}\}$ — перестановка
$\Rightarrow P_n\left(\frac{d}{dt}\right) = \left(\frac{d}{dt} - \lambda_{j_1} E\right) \circ \dots \circ \left(\frac{d}{dt} - \lambda_{j_n} E\right)$

### Теорема 6
Пусть $P_n(\lambda) = P_k(\lambda) \cdot P_{n-k}(\lambda)$
1) если $u(t)$ — решение $P_k\left(\frac{d}{dt}\right) u = 0 \Rightarrow u(t)$ — решение $P_n\left(\frac{d}{dt}\right) u = 0$
2) если $u(t)$ — решение $P_{n-k}\left(\frac{d}{dt}\right) u = 0 \Rightarrow u(t)$ — решение $P_n\left(\frac{d}{dt}\right) u = 0$

### Доказательство
$\square$:
1) $P_n\left(\frac{d}{dt}\right) = P_{n-k}\left(\frac{d}{dt}\right) P_k\left(\frac{d}{dt}\right)$
2) $P_n\left(\frac{d}{dt}\right) u = P_{n-k}\left(\frac{d}{dt}\right) \underbrace{P_k\left(\frac{d}{dt}\right) u}_{=0} = 0$
$\blacksquare$

 --- 

photo_2026-05-01 12.41.30 PM.jpeg -- 39

 --- 

$$ P_{n-k}\left(\frac{d}{dt}\right) P_k\left(\frac{d}{dt}\right) = P_k\left(\frac{d}{dt}\right) P_{n-k}\left(\frac{d}{dt}\right) = P_n\left(\frac{d}{dt}\right) $$
получаем справедливость п. 1.

Рассмотрим серию задач Коши; вначале введем семейство операторов:
$$ P_1\left(\frac{d}{dt}\right) = \left(\frac{d}{dt} - \lambda_1 E\right) $$
$$ P_2\left(\frac{d}{dt}\right) = \left(\frac{d}{dt} - \lambda_1 E\right) \left(\frac{d}{dt} - \lambda_2 E\right) $$
$$ P_k\left(\frac{d}{dt}\right) = \left(\frac{d}{dt} - \lambda_1 E\right) \dots \left(\frac{d}{dt} - \lambda_k E\right) $$

### Задачи Коши:
$$ \begin{cases} P_1\left(\frac{d}{dt}\right) u = 0 \\ u|_{t=0} = 1 \end{cases} \quad (\Pi. 1) $$

$$ \begin{cases} P_2\left(\frac{d}{dt}\right) u = 0 \\ u|_{t=0} = 0 \\ u'|_{t=0} = 1 \end{cases} \quad (\Pi. 2) $$

$$ \begin{cases} P_k\left(\frac{d}{dt}\right) u = 0 \\ u|_{t=0} = u'|_{t=0} = \dots = u^{(k-2)}|_{t=0} = 0 \\ u^{(k-1)}|_{t=0} = 1 \end{cases} \quad (\Pi. k) $$

### Th 7
- $\psi(t, \lambda_1)$ — реш $(\Pi. 1)$
- $\psi(t, \lambda_1, \lambda_2)$ — реш $(\Pi. 2)$
- $\psi(t, \lambda_1, \dots, \lambda_k)$ — реш $(\Pi. k)$

### Д: По индукции:
- База: $\psi(t, \lambda_1) = e^{\lambda_1 t}$ — реш $(\Pi. 1)$
- Предположение: $\psi(t, \lambda_1, \dots, \lambda_k)$ — реш $(\Pi. k)$
- Покажем, что $\psi(t, \lambda_1, \dots, \lambda_{k+1})$ — реш:
$$ \begin{cases} P_{k+1}\left(\frac{d}{dt}\right) u = 0 \\ u|_{t=0} = u'|_{t=0} = \dots = u^{(k-1)}|_{t=0} = 0 \\ u^{(k)}|_{t=0} = 1 \end{cases} $$
$$ P_{k+1}\left(\frac{d}{dt}\right) = \left(\frac{d}{dt} - \lambda_1 E\right) \dots \left(\frac{d}{dt} - \lambda_{k+1} E\right) $$

 --- 

photo_2026-05-01 12.41.31 PM.jpeg -- 40

 --- 

Из леммы 2 имеем:
$$ \frac{d}{dt} \psi(t, \lambda_1, \dots, \lambda_{k+1}) = \lambda_{k+1} \psi(t, \lambda_1, \dots, \lambda_{k+1}) + \psi(t, \lambda_1, \dots, \lambda_k) $$
$$ \psi(t, \lambda_1, \dots, \lambda_k) = \left( \frac{d}{dt} - \lambda_{k+1} \right) \psi(t, \lambda_1, \dots, \lambda_{k+1}) $$
$$ 0 = P_k\left(\frac{d}{dt}\right) \psi(t, \lambda_1, \dots, \lambda_k) = \left( \frac{d}{dt} - \lambda_1 E \right) \circ \dots \circ \left( \frac{d}{dt} - \lambda_k E \right) \left( \frac{d}{dt} - \lambda_{k+1} E \right) \psi(t, \dots) = P_{k+1}\left(\frac{d}{dt}\right) \psi(t, \dots) $$
Очевидно, что $\psi(0, \lambda_1, \dots, \lambda_{k+1}) = 0$.

$$ \left. \frac{d\psi}{dt} \right|_{t=0} = 0 $$
$$ [НРЗБ] $$
$$ \frac{d^{j+1}}{dt^{j+1}} \psi(t, \lambda_1, \dots, \lambda_{k+1}) = \lambda_{k+1} \frac{d^j}{dt^j} \psi(t, \lambda_1, \dots, \lambda_{k+1}) + \frac{d^j}{dt^j} \psi(t, \lambda_1, \dots, \lambda_k) $$
$$ \left. \frac{d^{j+1}}{dt^{j+1}} \psi(t, \lambda_1, \dots, \lambda_{k+1}) \right|_{t=0} = \lambda_{k+1} \left. \frac{d^j}{dt^j} \psi(t, \lambda_1, \dots, \lambda_{k+1}) \right|_{t=0} + \left. \left. \frac{d^j}{dt^j} \psi(t, \lambda_1, \dots, \lambda_k) \right|_{t=0} \right|_{t=0} $$

# 11.12.25 лекция

Если $\tilde{\lambda}_1, \dots, \tilde{\lambda}_n$ — разные:
$$ \psi(t, \tilde{\lambda}_1) = e^{\tilde{\lambda}_1 t} $$
$$ \psi(t, \tilde{\lambda}_1, \tilde{\lambda}_2) = \frac{\psi(t, \tilde{\lambda}_2) - \psi(t, \tilde{\lambda}_1)}{\tilde{\lambda}_2 - \tilde{\lambda}_1} $$
$$ \vdots $$
$$ \psi(t, \tilde{\lambda}_1, \dots, \tilde{\lambda}_{k-1}, \tilde{\lambda}_k) = \frac{\psi(t, \tilde{\lambda}_1, \dots, \tilde{\lambda}_{k-2}, \tilde{\lambda}_k) - \psi(t, \tilde{\lambda}_1, \dots, \tilde{\lambda}_{k-1})}{\tilde{\lambda}_k - \tilde{\lambda}_{k-1}} $$

$\vec{\psi}(t) = (\psi(t, \tilde{\lambda}_1, \dots, \tilde{\lambda}_i))$ — реш.
$$ \begin{cases} \frac{d\vec{\psi}}{dt} = \begin{pmatrix} \tilde{\lambda}_n & 1 & \mathbb{O} \\ 0 & \ddots & 1 \\ \mathbb{O} & 0 & \tilde{\lambda}_1 \end{pmatrix} \vec{\psi} \\ \left. \vec{\psi} \right|_{t=0} = \begin{pmatrix} 0 \\ \vdots \\ 0 \\ 1 \end{pmatrix} \end{cases} $$

$\tilde{\lambda}_1, \dots, \tilde{\lambda}_n$ — произвольные:
$$ \psi(t, \tilde{\lambda}_1) = e^{\tilde{\lambda}_1 t} $$
$$ \psi(t, \tilde{\lambda}_1, \dots, \tilde{\lambda}_k, \tilde{\lambda}_{k+1}) = \int_0^t e^{\tilde{\lambda}_{k+1}(t-s)} \psi(s, \tilde{\lambda}_1, \dots, \tilde{\lambda}_k) ds $$

 --- 

photo_2026-05-01 12.41.32 PM.jpeg -- 41

 --- 

$\psi(t | \tilde{\lambda}_1, \dots, \tilde{\lambda}_n) - \text{реш}$

$$
\begin{cases} 
P_n(\frac{d}{dt}) \psi = 0 \\ 
\psi|_{t=0} = \psi'|_{t=0} = \dots = \psi^{(n-2)}|_{t=0} = 0 \\ 
\psi^{(n-1)}|_{t=0} = 1 
\end{cases}
$$

$$P_k(\lambda) = (\lambda - \tilde{\lambda}_1) \dots (\lambda - \tilde{\lambda}_k)$$

## Th 8
Пусть $\tilde{\lambda}_1, \dots, \tilde{\lambda}_n$ — корни $P_n(\lambda) = 0 \Rightarrow \{ \psi(t | \tilde{\lambda}_1), \dots, \psi(t | \tilde{\lambda}_1, \dots, \tilde{\lambda}_n) \} - \text{ФСР для } (\Delta)$

### Доказательство $\square$
Нужно показать, что:
- 1) $\psi(t | \tilde{\lambda}_1), \dots, \psi(t | \tilde{\lambda}_1, \dots, \tilde{\lambda}_n) - \text{решения } (\Delta)$
- 2) $\psi(t | \tilde{\lambda}_1), \dots, \psi(t | \tilde{\lambda}_1, \dots, \tilde{\lambda}_n) - \text{ЛНЗ}$

Т.к. $P_n(\frac{d}{dt}) = P_k(\frac{d}{dt}) \circ (\frac{d}{dt} - \tilde{\lambda}_{k+1} E) \circ \dots \circ (\frac{d}{dt} - \tilde{\lambda}_n E)$, то в силу Th 6 и Th 7 получили, что $\{\psi(t | \tilde{\lambda}_1), \dots, \psi(t | \tilde{\lambda}_1, \dots, \tilde{\lambda}_n)\} - \text{реш } (\Delta)$ — поясняет справедливость пункта 1.

Пункт 2:
$$C_1 \psi(t | \tilde{\lambda}_1) + \dots + C_n \psi(t | \tilde{\lambda}_1, \dots, \tilde{\lambda}_n) = 0$$
$$\frac{d}{dt} (C_1 \psi(t | \tilde{\lambda}_1) + \dots + C_n \psi(t | \tilde{\lambda}_1, \dots, \tilde{\lambda}_n)) = 0$$
$$\dots$$
$$\frac{d^{n-1}}{dt^{n-1}} (C_1 \psi(t | \tilde{\lambda}_1) + \dots + C_n \psi(t | \tilde{\lambda}_1, \dots, \tilde{\lambda}_n)) = 0$$

$$
\begin{pmatrix} 
\psi(t | \tilde{\lambda}_1) & \dots & \psi(t | \tilde{\lambda}_1, \dots, \tilde{\lambda}_n) \\ 
\vdots & \ddots & \vdots \\ 
\frac{d^{n-1}}{dt^{n-1}} \psi(t | \tilde{\lambda}_1) & \dots & \frac{d^{n-1}}{dt^{n-1}} \psi(t | \tilde{\lambda}_1, \dots, \tilde{\lambda}_n) 
\end{pmatrix} 
\begin{pmatrix} 
C_1 \\ 
\vdots \\ 
C_n 
\end{pmatrix} = 
\begin{pmatrix} 
0 \\ 
\vdots \\ 
0 
\end{pmatrix}
$$

При $t = 0$:
$$
\begin{pmatrix} 
1 & \dots & 0 \\ 
* & \ddots & \vdots \\ 
* & * & 1 
\end{pmatrix} 
\begin{pmatrix} 
C_1 \\ 
\vdots \\ 
C_n 
\end{pmatrix} = 
\begin{pmatrix} 
0 \\ 
\vdots \\ 
0 
\end{pmatrix}
$$

Т.к. $\det \neq 0$, то $C_1 = \dots = C_n = 0$. $\blacksquare$

 --- 

photo_2026-05-01 12.41.45 PM.jpeg -- 42

 --- 

$$ \psi(t; \tilde{L}_1, \dots, \tilde{L}_n) \text{ — реш.} $$
$$ P_n\left(\frac{d}{dt}\right) \psi = 0 $$
$$ \begin{cases} \psi|_{t=0} = \psi'|_{t=0} = \dots = \psi^{(n-2)}|_{t=0} = 0 \\ \psi^{(n-1)}|_{t=0} = 1 \end{cases} $$
$$ P_k(\lambda) = (\lambda - \tilde{L}_1) \dots (\lambda - \tilde{L}_k) $$

### Теорема 8
Пусть $\tilde{L}_1, \dots, \tilde{L}_n$ — корни $P_n(\lambda) = 0 \implies \{ \psi(t; \tilde{L}_1), \psi(t; \tilde{L}_1, \tilde{L}_2), \dots, \psi(t; \tilde{L}_1, \dots, \tilde{L}_n) \}$ — ФСР для $(\Delta)$.

### Доказательство
Нужно показать, что:
1) $\psi(t; \tilde{L}_1), \psi(t; \tilde{L}_1, \tilde{L}_2), \dots, \psi(t; \tilde{L}_1, \dots, \tilde{L}_n)$ — реш. $(\Delta)$
2) $\psi(t; \tilde{L}_1), \dots, \psi(t; \tilde{L}_1, \dots, \tilde{L}_n)$ — лнз

Т.к. $P_n\left(\frac{d}{dt}\right) = P_k\left(\frac{d}{dt}\right) \circ \left(\frac{d}{dt} - \tilde{L}_{k+1} E\right) \circ \dots \circ \left(\frac{d}{dt} - \tilde{L}_n E\right)$, то в силу Th 6 и Th 7 получили, что $\{ \psi(t; \tilde{L}_1), \dots, \psi(t; \tilde{L}_1, \dots, \tilde{L}_n) \}$ — реш. $(\Delta)$.

Рассмотрим справедливость **пункта 2**.
$$ C_1 \psi(t; \tilde{L}_1) + \dots + C_n \psi(t; \tilde{L}_1, \dots, \tilde{L}_n) = 0 $$
$$ C_1 \frac{d}{dt} \psi(t; \tilde{L}_1) + \dots + C_n \frac{d}{dt} \psi(t; \tilde{L}_1, \dots, \tilde{L}_n) = 0 $$
$$ \dots $$
$$ C_1 \frac{d^{n-1}}{dt^{n-1}} \psi(t; \tilde{L}_1) + \dots + C_n \frac{d^{n-1}}{dt^{n-1}} \psi(t; \tilde{L}_1, \dots, \tilde{L}_n) = 0 $$

$$ \begin{pmatrix} \psi(t; \tilde{L}_1) & \dots & \psi(t; \tilde{L}_1, \dots, \tilde{L}_n) \\ \vdots & \ddots & \vdots \\ \frac{d^{n-1}}{dt^{n-1}} \psi(t; \tilde{L}_1) & \dots & \frac{d^{n-1}}{dt^{n-1}} \psi(t; \tilde{L}_1, \dots, \tilde{L}_n) \end{pmatrix} \begin{pmatrix} C_1 \\ \vdots \\ C_n \end{pmatrix} = \begin{pmatrix} 0 \\ \vdots \\ 0 \end{pmatrix} $$

При $t=0$:
$$ \begin{pmatrix} 1 & 0 & \dots & 0 \\ * & 1 & \dots & 0 \\ \vdots & \vdots & \ddots & \vdots \\ * & * & \dots & 1 \end{pmatrix} \begin{pmatrix} C_1 \\ \vdots \\ C_n \end{pmatrix} = \begin{pmatrix} 0 \\ \vdots \\ 0 \end{pmatrix} $$

Т.к. $\det \neq 0$, то $C_1 = \dots = C_n = 0$. $\blacksquare$

 --- 

photo_2026-05-01 12.41.48 PM.jpeg -- 43

 --- 

# Св-ва пси функций

- 1) $\psi(t; \tilde{t}_1, \dots, \tilde{t}_k)$ непрерывно зависит от $\tilde{t}_1, \dots, \tilde{t}_k$, $k=1, \dots, n$
### Опр.
Из того, что $\psi(t; \tilde{t}_1, \dots, \tilde{t}_k)$ — решение ЗК

- 2) Пусть $\{j_1, \dots, j_k\}$ — перестановка $\implies \psi(t; \tilde{t}_1, \dots, \tilde{t}_k) = \psi(t; \tilde{t}_{j_1}, \dots, \tilde{t}_{j_k})$
### Опр.
Из Th 7

- 3) $\psi(t; \underbrace{\tilde{t}, \dots, \tilde{t}}_{k}) = \frac{t^{k-1} e^{\tilde{t} t}}{(k-1)!}$
### Доказательство
Индукцией из интегрального представления

- 4) Пусть $\tilde{t}_1, \dots, \tilde{t}_k$ — различны $\implies \psi(t; \tilde{t}_1, \dots, \tilde{t}_k) = \sum_{i=1}^k A_i \cdot \psi(t; \tilde{t}_i)$, где
$$A_i = \frac{1}{\prod_{j \neq i}^k (\tilde{t}_i - \tilde{t}_j)}$$
### Опр.
Из формулы разделенной разности

- 5) Пусть $\tilde{t}_k \neq \tilde{t}_{k+1}$
$$\psi(t; \tilde{t}_1, \dots, \tilde{t}_k, \tilde{t}_{k+1}) = \frac{\psi(t; \tilde{t}_1, \dots, \tilde{t}_{k-1}, \tilde{t}_{k+1}) - \psi(t; \tilde{t}_1, \dots, \tilde{t}_{k-1}, \tilde{t}_k)}{\tilde{t}_{k+1} - \tilde{t}_k}$$
### Опр.
Из формулы разделенной разности и свойства 2

- 6) Пусть $\{\tilde{t}_1, \dots, \tilde{t}_n\} = \{\alpha_1, \dots, \alpha_p\} \cup \{\beta_1, \dots, \beta_q\}$, $p+q=n$
$\alpha_i \neq \beta_j, i=1..p, j=1..q$
$$\psi(t; \tilde{t}_1, \dots, \tilde{t}_n) = \sum_{i=1}^p A_i \psi(t; \alpha_i, \alpha_1, \dots, \alpha_p) + \sum_{j=1}^q B_j \psi(t; \beta_j, \beta_1, \dots, \beta_q)$$

### Доказательство
Докажем по индукции по $k$
База: $\psi(t; \tilde{t}_1) = e^{\tilde{t}_1 t}$
Пусть $\tilde{t}_1, \dots, \tilde{t}_k = \begin{cases} \tilde{t}_i \in \{\alpha_1, \dots, \alpha_p\} \\ \tilde{t}_j \in \{\beta_1, \dots, \beta_q\} \end{cases}$

$$\psi(t; \tilde{t}_1, \dots, \tilde{t}_n) = \psi(t; \alpha_1, \dots, \alpha_p, \beta_1, \dots, \beta_q) \stackrel{\text{②}}{=}$$
$$\stackrel{\text{⑤}}{=} \frac{\psi(t; \alpha_1, \dots, \alpha_p, \beta_1, \dots, \beta_{j-1}, \beta_{j+1}, \dots, \beta_q) - \psi(t; \alpha_1, \dots, \alpha_{i-1}, \alpha_{i+1}, \dots, \alpha_p, \beta_1, \dots, \beta_q)}{\alpha_i - \beta_j} \stackrel{\text{пред. инд.}}{=}$$
$$= \frac{\psi(t; \alpha_i, \alpha_1, \dots, \alpha_p, \beta_1, \dots, \beta_{j-1}, \dots) - \psi(t; \alpha_1, \dots, \alpha_{i-1}, \dots, \beta_j, \dots, \beta_q)}{\alpha_i - \beta_j} = \dots$$
[НРЗБ: стрелки к пред. инд.]

 --- 

photo_2026-05-01 12.41.50 PM.jpeg -- 44

 --- 

# Th 9

### Теорема
Пусть $P_n(\lambda) = P_{k_1}(\lambda) \cdot \dots \cdot P_{k_l}(\lambda)$, где $P_{k_1}(\lambda), \dots, P_{k_l}(\lambda)$ — попарно взаимно простые (т. е. не имеют общих корней).
$M_1 = \{ u_1^1(t), \dots, u_{k_1}^1(t) \}$ — ФСР для $P_{k_1}(\frac{d}{dt})u = 0$
$\dots$
$M_l = \{ u_1^l(t), \dots, u_{k_l}^l(t) \}$ — ФСР для $P_{k_l}(\frac{d}{dt})u = 0$
$\Rightarrow M = \bigcup_{i=1}^l M_i$ — ФСР $(\Delta)$

### Доказательство
Покажем по индукции по $l$.
Пусть $l=2$.
$P_n(\lambda) = P_{k_1}(\lambda) \cdot P_{k_2}(\lambda)$, $P_{k_1}(\lambda)$ и $P_{k_2}(\lambda)$ — взаимно простые.
$M_1 = \{ u_1^1(t), \dots, u_{k_1}^1(t) \}$ — ФСР $P_{k_1}(\frac{d}{dt})u = 0$
$M_2 = \{ u_1^2(t), \dots, u_{k_2}^2(t) \}$ — ФСР $P_{k_2}(\frac{d}{dt})u = 0$
Мы покажем, что $\{ \psi(t, \lambda_1), \dots, \psi(t, \lambda_1, \dots, \lambda_n) \}$ линейно выражаются (конкретно) через функции из $M = M_1 \cup M_2$.
Пусть $\alpha_1, \dots, \alpha_{k_1}$ — корни $P_{k_1}(\lambda) = 0$.
$\beta_1, \dots, \beta_{k_2}$ — корни $P_{k_2}(\lambda) = 0$.
$\{ \psi(t, \alpha_1), \dots, \psi(t, \alpha_1, \dots, \alpha_{k_1}) \}$ — ФСР для $P_{k_1}(\frac{d}{dt})u = 0$.
Все элементы из $\{ \psi(t, \alpha_1), \dots, \psi(t, \alpha_1, \dots, \alpha_{k_1}) \}$ линейно выражаются через элементы $M_1, \text{ в } [НРЗБ]$.
Все элементы из $\{ \psi(t, \beta_1), \dots, \psi(t, \beta_1, \dots, \beta_{k_2}) \}$ выражаются линейно через элементы $M_2$.
По св-ву [НРЗБ: 6] $\psi(t, \bar{\lambda}_1, \dots, \bar{\lambda}_n)$ линейно выражаются через элементы $\{ \psi(t, \alpha_1), \dots, \psi(t, \alpha_1, \dots, \alpha_{k_1}) \}$ и $\{ \psi(t, \beta_1), \dots, \psi(t, \beta_1, \dots, \beta_{k_2}) \}$.
Значит все элементы ФСР $\{ \psi(t, \bar{\lambda}_1), \dots, \psi(t, \bar{\lambda}_1, \dots, \bar{\lambda}_n) \}$ линейно выражаются через элементы $M_1 \cup M_2$ и $u_j^i(t)$ — реш $(\Delta)$ в силу Th 6.
Пусть $l=3$.
$P_n(\lambda) = \underbrace{P_{k_1}(\lambda) \cdot P_{k_2}(\lambda)}_{P_{k_1+k_2}(\lambda)} \cdot P_{k_3}(\lambda)$.
Ну и этот же механизм.

# Th 10
Пусть [НРЗБ]
$M_1 = [НРЗБ]$
$\dots$
$M_l = [НРЗБ]$
$y^{(n)}$
$g: [НРЗБ]$

### Опр.
1) [НРЗБ]
2) [НРЗБ]
3) [НРЗБ]
$z(t) = [НРЗБ]$

### Рассмотрим [НРЗБ]
$$ \begin{cases} y^{(n)} = [НРЗБ] \\ y|_{t=t_0} = [НРЗБ] \\ y'|_{t=t_0} = [НРЗБ] \\ \dots \\ y^{(n-1)}|_{t=t_0} = [НРЗБ] \end{cases} $$

# Th 1
Пусть [НРЗБ]

 --- 

photo_2026-05-01 12.41.54 PM.jpeg -- 45

 --- 

### Th 10
Пусть $\lambda_1$ — корень $P_n(\lambda) = 0$ кр-ти $k_1$,
..., $\lambda_l$ — корень $P_n(\lambda) = 0$ кр-ти $k_l$. $k_1 + \dots + k_l = n$.
$$M_1 = \left\{ e^{\lambda_1 t}, t e^{\lambda_1 t}, \dots, \frac{t^{k_1-1}}{(k_1-1)!} e^{\lambda_1 t} \right\}$$
...
$$M_l = \left\{ e^{\lambda_l t}, t e^{\lambda_l t}, \dots, \frac{t^{k_l-1}}{(k_l-1)!} e^{\lambda_l t} \right\}$$
$$M = \bigcup_{i=1}^l M_i \text{ — ФСР для } (\Delta)$$

## § 4 Диф. ур-ия высокого порядка [НРЗБ]

$$y^{(n)} = g(t, y, y', \dots, y^{(n-1)}) \quad (1)$$
$g: \Omega \to \mathbb{R}$, обл. $\Omega \subseteq \mathbb{R}^{n+1}$

### Опр.
Реш. ур-я (1) — функция $y(t)$, опред. на $\langle \alpha, \omega \rangle$:
- 1) $y(t) \in C^n(\langle \alpha, \omega \rangle)$
- 2) $(t, y(t), y'(t), \dots, y^{(n-1)}(t)) \in \Omega, \quad t \in \langle \alpha, \omega \rangle$
- 3) $\frac{d^n}{dt^n} y(t) \equiv g(t, y(t), \frac{d}{dt} y(t), \dots, \frac{d^{n-1}}{dt^{n-1}} y(t)) \quad \forall t \in \langle \alpha, \omega \rangle$

$$z(t) = \begin{pmatrix} y(t) \\ y'(t) \\ \dots \\ y^{(n-1)}(t) \end{pmatrix} = \begin{pmatrix} z_1(t) \\ z_2(t) \\ \dots \\ z_n(t) \end{pmatrix}; \quad \frac{dz}{dt} = \begin{pmatrix} z_2(t) \\ z_3(t) \\ \dots \\ z_n(t) \\ g(t, z_1(t), \dots, z_n(t)) \end{pmatrix} \quad (2)$$

Рассмотрим ЗК
$$\begin{cases} y^{(n)} = g(t, y, y', \dots, y^{(n-1)}) \\ y|_{t=t_0} = y_0^1 \\ y'|_{t=t_0} = y_0^2 \\ \dots \\ y^{(n-1)}|_{t=t_0} = y_0^n \end{cases} (3) \sim \begin{cases} \frac{dz}{dt} = \begin{pmatrix} z_2 \\ \dots \\ z_n \\ g(t, z_1, \dots, z_n) \end{pmatrix} \\ z|_{t=t_0} = \begin{pmatrix} y_0^1 \\ \dots \\ y_0^n \end{pmatrix} \end{cases}$$

### Th 1
Пусть:
- 1) $g(t, z_1, \dots, z_n) \in C(\Omega)$
- 2) $g(t, z_1, \dots, z_n)$ локально липшицева по $z_1, \dots, z_n$ в $\Omega$
($\forall$ компакта $K \subseteq \Omega \ \exists L(K) \mid \forall (t, z_1, \dots, z_n), (t, \tilde{z}_1, \dots, \tilde{z}_n) \in K$)
$$|g(t, z_1, \dots, z_n) - g(t, \tilde{z}_1, \dots, \tilde{z}_n)| \le L(K) \sqrt{\sum_{i=1}^n (z_i - \tilde{z}_i)^2}$$

 --- 

photo_2026-05-01 12.41.55 PM.jpeg -- 46

 --- 

# Линейные дифференциальные уравнения $n$-го порядка

$\Rightarrow \exists!$ непродолжаемое решение ЗК (3)

$$u^{(n)} + a_1(t) u^{(n-1)} + \dots + a_n(t) u = \varphi(t) \quad (4)$$

$$z(t) = \begin{pmatrix} z_1(t) \\ \vdots \\ z_n(t) \end{pmatrix} = \begin{pmatrix} u(t) \\ u'(t) \\ \vdots \\ u^{(n-1)}(t) \end{pmatrix} \Rightarrow \frac{dz}{dt} = \begin{pmatrix} z_2 \\ \vdots \\ z_n \\ -a_n(t) z_1 - \dots - a_1(t) z_n + \varphi(t) \end{pmatrix} \quad (6)$$

Можно переписать:
$$\frac{dz}{dt} = A(t) z + f(t); \quad A(t) = \begin{pmatrix} 0 & 1 & 0 & \dots & 0 \\ 0 & 0 & 1 & \dots & 0 \\ \vdots & \vdots & \vdots & \ddots & \vdots \\ -a_n(t) & -a_{n-1}(t) & \dots & \dots & -a_1(t) \end{pmatrix}; \quad f(t) = \begin{pmatrix} 0 \\ \vdots \\ 0 \\ \varphi(t) \end{pmatrix}$$

$(4) \sim (6)$

$$P_n(t, \frac{d}{dt}) = \frac{d^n}{dt^n} + a_1(t) \frac{d^{n-1}}{dt^{n-1}} + \dots + a_n(t) E$$

$(4) \sim P_n(t, \frac{d}{dt}) u = \varphi(t)$

### Тн 2
Пусть $\varphi(t) \equiv 0$, $a_i(t) \in C(a, b) \Rightarrow$ множество решений, определенных на $(a, b)$, образует линейное пространство размерности $n$.

### Доказательство
$P_n(t, \frac{d}{dt}) u = 0 \sim \frac{dz}{dt} = A(t) z \quad (6) \Rightarrow$ мн-во реш (6) образуют лин. пространство размерности $n$.
$a_i(t) \in C(a, b) \Rightarrow A(t) \in C(a, b)$.

### Опр.
**Фундаментальная система решений** (ФСР) для (4) при $\varphi = 0$ — базис пространства решений ($n$ лин. нез. реш).

### Опр.
Пусть $\{u^1(t), \dots, u^n(t)\}$ — ФСР для (4) при $\varphi = 0$.
$$\begin{pmatrix} u^1 & \dots & u^n \\ (u^1)' & \dots & (u^n)' \\ \vdots & \vdots & \vdots \\ (u^1)^{(n-1)} & \dots & (u^n)^{(n-1)} \end{pmatrix} \text{ — ФМР для (4) при } \varphi = 0$$

### Замечание
ФМР для (4) при $\varphi = 0$ — это ФМР (6).

### Тн 3 (Остроградского–Лиувилля)
Пусть $\varphi \equiv 0$, $a_i \in C(a, b)$, $i = 1, \dots, n$; $u^1(t), \dots, u^n(t)$. Рассмотрим функцию:
$$\det \begin{pmatrix} u^1 & \dots & u^n \\ \vdots & \vdots & \vdots \\ (u^1)^{(n-1)} & \dots & (u^n)^{(n-1)} \end{pmatrix} \equiv W(t) \text{ — определитель Вронского}$$
$\Rightarrow W(t) = e^{-\int_{t_0}^t a_1(s) ds} W(t_0)$ — формула Остроградского–Лиувилля.

 --- 

photo_2026-05-01 12.41.56 PM.jpeg -- 47

 --- 

$\square$: (4) при $\varphi \equiv 0 \sim \frac{dz}{dt} = A(t)z$ (6)

$$\begin{pmatrix} u^1 & \dots & u^n \\ (u^1)' & \dots & (u^n)' \\ \vdots & \dots & \vdots \\ (u^1)^{(n-1)} & \dots & (u^n)^{(n-1)} \end{pmatrix} \text{ — реш (6)}$$

$$W(t) = e^{\int_{t_0}^t \operatorname{tr} A(s) \, ds} W(t_0)$$

$W(t)$ — опр. Вронского для (6). По формуле Остроградского–Лиувилля для системы (6) получим $W(t) = e^{\int_{t_0}^t \operatorname{tr} A(s) \, ds} W(t_0) = e^{-\int_{t_0}^t a_1(s) \, ds} W(t_0)$. $\square$

### Th 4
Пусть $a_i(t) \in C(a, b); \varphi(t) \in C(a, b)$,
1) $\{u^1(t), \dots, u^n(t)\}$ — ФСР для $P_n(t, \frac{d}{dt})u = 0$
2) $u_ч(t)$ — реш (4)
$\Rightarrow$ любое реш (4) имеет след. вид: $u(t) = u_ч(t) + \sum_{i=1}^n c_i u^i(t)$ (7)

### Доказательство
$\square$: От противного. Пусть $u(t)$ — реш (4), которое не выражается через (7).
Рассмотрим $v(t) = u(t) - u_ч(t)$
$$P_n(t, \frac{d}{dt})v(t) = P_n(t, \frac{d}{dt})(u(t) - u_ч(t)) = P_n(t, \frac{d}{dt})u(t) - P_n(t, \frac{d}{dt})u_ч(t) = \varphi(t) - \varphi(t) = 0$$
$v(t)$ — реш $P_n(t, \frac{d}{dt})v = 0 \Rightarrow \exists c_1, \dots, c_n \mid v(t) = \sum_{i=1}^n c_i u^i(t) = u(t) - u_ч(t)$
$\Rightarrow u(t) = u_ч(t) + \sum_{i=1}^n c_i u^i(t)$ [НРЗБ: противоречие]. $\square$

Рассмотрим ЗК Коши для (4)
$$\begin{cases} u^{(n)} + a_1(t)u^{(n-1)} + \dots + a_n(t)u = \varphi(t) \\ u|_{t=t_0} = u_1^0 \\ u'|_{t=t_0} = u_2^0 \\ \dots \\ u^{(n-1)}|_{t=t_0} = u_n^0 \end{cases} \quad (8)$$

### Th 5
Пусть $a_i(t) \in C(a, b), i = 1, \dots, n; \varphi(t) \in C(a, b) \Rightarrow \forall u_1^0, \dots, u_n^0 \exists!$ реш ЗК (8) опред на $(a, b)$

### Доказательство
$\square$: $z(t) = \begin{pmatrix} u(t) \\ u'(t) \\ \vdots \\ u^{(n-1)}(t) \end{pmatrix};$ (8) $\sim \frac{dz}{dt} = A(t)z + F(t); z|_{t=t_0} = \begin{pmatrix} u_1^0 \\ \vdots \\ u_n^0 \end{pmatrix}; A(t) = \begin{pmatrix} 0 & 1 & \dots & 0 \\ \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & \dots & 1 \\ -a_n & -a_{n-1} & \dots & -a_1 \end{pmatrix}$

$F(t) = \begin{pmatrix} 0 \\ \vdots \\ 0 \\ \varphi(t) \end{pmatrix}$ По Th Пикара имеем $\exists!$ $\square$

 --- 

photo_2026-05-01 12.41.57 PM (1).jpeg -- 48

 --- 

# 4 СЕМЕСТР

## Глава 3 Краевые задачи для линейных д.у.

### 1) Краевая задача на прямой ($A = const$)
$$
\begin{cases} 
\frac{dy}{dt} = Ay + f(t), t \in \mathbb{R} \\ 
\sup \|y(t)\| < \infty 
\end{cases}
$$

$$
\begin{cases} 
P_n \left( \frac{d}{dt} \right) u = h(t), t \in \mathbb{R} \\ 
\sup |u(t)| < \infty 
\end{cases}
$$
- модуля достаточно

### 2) Краевая задача на полупрямой
$$
\begin{cases} 
\frac{dy}{dt} = Ay + f(t), t > 0 \\ 
B y \big|_{t=0} = \psi, \quad B - m \times n \\ 
\sup_{t>0} \|y(t)\| < \infty 
\end{cases}
$$

$$
\begin{cases} 
P_n \left( \frac{d}{dt} \right) u = h(t), t > 0 \\ 
b_{1i} u(0) + b_{2i} u'(0) + \dots + b_{ni} u^{(n-1)}(0) = \psi_i \\ 
\sup_{t>0} |u(t)| < \infty 
\end{cases}
$$

### 3) Краевая задача на интервале
$$
\begin{cases} 
\frac{dy}{dt} = Ay + h(t), t \in (a, b) \\ 
L y\big|_{t=a} + R y\big|_{t=b} = \psi 
\end{cases}
$$
- $L, R - n \times n$
- тут ещё одна

 --- 

photo_2026-05-01 12.41.59 PM.jpeg -- 49

 --- 

## § 1 Краевая задача на прямой

$$\frac{dy}{dt} = Ay + f(t) \quad (1)$$

$$\begin{cases} \frac{dy}{dt} = Ay + f(t), \quad t \in \mathbb{R} \\ \sup_{t \in \mathbb{R}} \|y(t)\| < \infty \end{cases} \quad (2)$$

$f(t)$ — огр. и непр.

### Пример

$$\begin{cases} \frac{dy}{dt} = iy + e^{i \gamma t}, \quad t \in \mathbb{R} \\ \sup_{t \in \mathbb{R}} |y(t)| < \infty \end{cases}$$

1) $\gamma = 1$
$y(t) = c e^{it} + t e^{it}$ — нет ограниченных решений.

2) $\gamma \neq 1$
$y(t) = c e^{it} + \frac{i}{1 - \gamma} e^{i \gamma t}$ — $\infty$ много огр. реш.

### Предположение (*)

$$\forall \lambda \in \operatorname{Sp} A \quad \operatorname{Re} \lambda \neq 0 \Rightarrow \exists \delta > 0 \quad \forall \lambda \in \operatorname{Sp} A \quad \delta < |\operatorname{Re} \lambda| \quad (3)$$

### Th №1

Пусть выполнено предположение (*) $\Rightarrow \forall$ огр. $f(t) \in C(\mathbb{R})$ $\exists!$ решение краевой задачи (2), при этом справедлива оценка:
$$\sup_{t \in \mathbb{R}} \|y(t)\| \leq C \cdot \sup_{t \in \mathbb{R}} \|f(t)\| \quad (4)$$

### Д: Рассмотрим 3 случая

1) $\forall \lambda \in \operatorname{Sp} A \quad \operatorname{Re} \lambda < 0$

2) $\forall \lambda \in \operatorname{Sp} A \quad \operatorname{Re} \lambda > 0$

3) Общий случай

 --- 

photo_2026-05-01 12.42.00 PM.jpeg -- 50

 --- 

# 1-й случай

$$ \forall \lambda \in \operatorname{Sp} A \quad \operatorname{Re} \lambda < 0 $$

(3) $\Rightarrow \exists \delta > 0 \quad \forall \lambda \in \operatorname{Sp} A \quad \operatorname{Re} \lambda < -\delta$ (5)

Общее решение (1) имеет вид $y(t) = e^{tA}c + \int_0^t e^{(t-s)A} f(s) \, ds$, $c = \begin{pmatrix} c_1 \\ \vdots \\ c_n \end{pmatrix}$.

Используя (5), в силу оценки Гельфанда–Шилова получим:
$$ \| e^{tA} \| \le e^{-\delta t} \left( 1 + \frac{2 \|A\| t}{1!} + \dots + \frac{(2 \|A\| t)^{n-1}}{(n-1)!} \right), t \ge 0 \quad (6) $$
$\Rightarrow \| e^{tA} \| \le e^{-\frac{\delta}{2} t} M(\delta, A), t \ge 0$ (7), $M(\delta, A) > 0$ — const.

$$ \|y(t)\| \le \|e^{tA}\| \cdot \|c\| + \int_0^t \|e^{(t-s)A}\| \cdot \|f(s)\| \, ds \quad (8) $$

Обозначим $F = \sup_{t \in \mathbb{R}} \|f(t)\|$. При $t \ge 0$: 
$$ \|y(t)\| \le e^{-\frac{\delta}{2}t} M(\delta, A) \cdot \|c\| + F \cdot M(\delta, A) \int_0^t e^{-\frac{\delta}{2}(t-s)} \, ds = $$
$$ = M(\delta, A) \left( \|c\| e^{-\frac{\delta}{2}t} + \frac{2F}{\delta} (1 - e^{-\frac{\delta}{2}t}) \right) (t \ge 0) $$
$\Rightarrow$ все решения (1) ограничены при $t \ge 0$.

Покажем, что $\exists!$ реш. (1), ограниченное при $t < 0$. Предположим $\exists c_0$ (вектор): при $c = c_0 \quad y(t)$ ограничено при $t < 0$. Т.е.:
$y(t) = e^{tA} c_0 + \int_0^t e^{(t-s)A} f(s) \, ds$ — ограничено при $t < 0$. 

При $t < 0$:
$$ \|e^{-tA}\| \le e^{\delta t} \left( 1 + \frac{-2 \|A\| t}{1!} + \dots + \frac{(-2 \|A\| t)^{n-1}}{(n-1)!} \right) \xrightarrow{t \to -\infty} 0 $$
$y(t)$ ограничено при $t < 0 \Rightarrow \|e^{-tA} y(t)\| \xrightarrow{t \to -\infty} 0 \sim \| c_0 + \int_0^t e^{-sA} f(s) \, ds \| \xrightarrow{t \to -\infty} 0 \sim$
$\sim c_0 = \int_0^{-\infty} e^{-sA} f(s) \, ds$. Подставив в формулу для $y(t)$, получим:
$$ y(t) = \int_{-\infty}^t e^{(t-s)A} f(s) \, ds \text{ — кандидат на ограниченное решение} $$
$$ \|y(t)\| \le \int_{-\infty}^t \| e^{(t-s)A} \| \cdot \|f(s)\| \, ds \stackrel{(7)}{\le} F \cdot M(\delta, A) \int_{-\infty}^t e^{-\frac{\delta}{2}(t-s)} \, ds = \frac{2 M(\delta, A)}{\delta} F $$
Это справедливо при $t \in \mathbb{R}$, и это и есть (4).

# 2-й случай

$$ \forall \lambda \in \operatorname{Sp} A \quad \operatorname{Re} \lambda > 0 \sim \forall \lambda \in \operatorname{Sp} (-A) \quad \operatorname{Re} \lambda < 0 $$
Замена $t = -s, \quad y(t) = y(-s) = \tilde{y}(s) = \tilde{y}(-t)$.
$\frac{dy}{dt}, \frac{d\tilde{y}}{ds}$ тогда:
$$ (2) \sim \begin{cases} \frac{d\tilde{y}}{ds} = \tilde{A}\tilde{y} + \tilde{f}(s), \quad s \in \mathbb{R} \\ \sup_{s \in \mathbb{R}} \|\tilde{y}(s)\| < \infty \end{cases} $$

 --- 

photo_2026-05-01 12.42.01 PM.jpeg -- 51

 --- 

# Обыкновенные дифференциальные уравнения

$\tilde{A} = -A$; $\tilde{f}(s) = -f(-s)$; $\forall \lambda \in \operatorname{Sp} A \quad \operatorname{Re} \lambda < 0$ (случай 1)
$\Rightarrow \exists!$ реш. кр. з. $\tilde{y}(s) = \int_{-\infty}^s e^{(s-\tau)\tilde{A}} \tilde{f}(\tau) \, d\tau$
$\Rightarrow \exists!$ реш. кр. з. (2)
$y(t) = y^+(t) = \int_{-\infty}^t e^{(t-\tau)A} f(\tau) \, d\tau = -\int_{+\infty}^{-t} e^{(t+\tilde{\tau})A} f(-\tilde{\tau}) \, d\tilde{\tau} = -\int_t^\infty e^{(t-s)A} f(s) \, ds$
Так же в силу эквивалентности есть оценка (4).

## 3-й случай

$\lambda_1, \dots, \lambda_m \in \operatorname{Sp} A : \operatorname{Re} \lambda_i < 0 \quad i=1, \dots, m$
$\lambda_{m+1}, \dots, \lambda_n \in \operatorname{Sp} A : \operatorname{Re} \lambda_i > 0 \quad i=m+1, \dots, n$

$$TAT^{-1} = \begin{pmatrix} A_- & 0 \\ 0 & A_+ \end{pmatrix}$$

- $A_- \text{ — } m \times m$; $\operatorname{Sp} A_- = \{ \lambda_1, \dots, \lambda_m \}$
- $A_+ \text{ — } (n-m) \times (n-m)$; $\operatorname{Sp} A_+ = \{ \lambda_{m+1}, \dots, \lambda_n \}$

Замена:
$$\frac{dy}{dt} = T^{-1} \begin{pmatrix} A_- & 0 \\ 0 & A_+ \end{pmatrix} Ty + f(t)$$
$$T \frac{dy}{dt} = \begin{pmatrix} A_- & 0 \\ 0 & A_+ \end{pmatrix} Ty + Tf(t)$$
Итог (замена): $\begin{pmatrix} v_-(t) \\ v_+(t) \end{pmatrix} = v(t) = Ty(t)$

После замены распадается:
$$ \begin{cases} \frac{dv_-}{dt} = A_- v_- + \tilde{f}_-(t) \\ \sup_{t \in \mathbb{R}} \| v_-(t) \| < \infty \end{cases} \implies \text{ случай 1} $$
$$ \begin{cases} \frac{dv_+}{dt} = A_+ v_+ + \tilde{f}_+(t) \\ \sup_{t \in \mathbb{R}} \| v_+(t) \| < \infty \end{cases} \implies \text{ случай 2} $$

Где $\begin{pmatrix} \tilde{f}_-(t) \\ \tilde{f}_+(t) \end{pmatrix} = Tf(t)$.

Тогда склеиваем и получаем желаемое. $\blacksquare$

### Опр. Функция Хевисайда
$$\theta(t) = \begin{cases} 1, & t \ge 0 \\ 0, & t < 0 \end{cases}$$

### Случай 1
$\forall \lambda \in \operatorname{Sp} A \quad \operatorname{Re} \lambda < 0$
$$y(t) = \int_{-\infty}^{t} e^{(t-s)A} f(s) \, ds = \int_{-\infty}^{\infty} \theta(t-s) e^{(t-s)A} f(s) \, ds$$
$$G(t) = \begin{cases} e^{tA}, & t > 0 \\ 0, & t < 0 \end{cases}$$
$$y(t) = \int_{-\infty}^{\infty} G(t-s) f(s) \, ds \quad (9)$$

---
*(Правая колонка)*

### Случай 2
$y(t) = [НРЗБ]$
$G(t) = [НРЗБ]$

### Случай 3
$y(t) = \dots$
$= \int_{-\infty}^{\infty} T^{-1} [НРЗБ] T f(s) \, ds$
$= \int_{-\infty}^{\infty} [НРЗБ] f(s) \, ds$

Решение:
$G(t) = [НРЗБ]$

### Свойства G(t)
1) $\frac{d}{dt} G(t) = AG(t)$
2) $G(+0) - G(-0) = E$
3) $\sup_{t \in \mathbb{R}} \|G(t)\| < \infty$

### Опр.
Матрица [НРЗБ] называется матрицей Грина [НРЗБ] задачи (2).
Th 2
Пусть [НРЗБ] задачи (2)
[НРЗБ]
1) Из [НРЗБ]
2) Из [НРЗБ]

 --- 

photo_2026-05-01 12.42.02 PM.jpeg -- 52

 --- 

### Случай 2
$$\forall \lambda \in \operatorname{sp} A \quad \operatorname{Re} \lambda > 0$$
$$y(t) = -\int_{t}^{\infty} e^{(t-s)A} f(s) ds = \int_{-\infty}^{\infty} (-\theta(s-t) e^{(t-s)A}) f(s) ds$$
$$G(t) = \begin{cases} 0, & t > 0 \\ -e^{tA}, & t < 0 \end{cases}$$
реш. имеет вид (3)

### Случай 3
$$TAT^{-1} = \begin{pmatrix} A_- & 0 \\ 0 & A_+ \end{pmatrix}$$
$$y(t) = T^{-1} \begin{pmatrix} V_-(t) \\ V_+(t) \end{pmatrix} = \int_{-\infty}^{\infty} T^{-1} \begin{pmatrix} \theta(t-s) e^{(t-s)A_-} & 0 \\ 0 & -\theta(s-t) e^{(t-s)A_+} \end{pmatrix} \begin{pmatrix} f_-(s) \\ f_+(s) \end{pmatrix} ds =$$
$$= \int_{-\infty}^{\infty} \left[ T^{-1} \begin{pmatrix} \theta(t-s) e^{(t-s)A_-} & 0 \\ 0 & -\theta(s-t) e^{(t-s)A_+} \end{pmatrix} T \right] f(s) ds$$
Решение имеет вид (3):
$$G(t) = \begin{cases} T^{-1} \begin{pmatrix} e^{tA_-} & 0 \\ 0 & 0 \end{pmatrix} T, & t > 0 \\ -T^{-1} \begin{pmatrix} 0 & 0 \\ 0 & e^{tA_+} \end{pmatrix} T, & t < 0 \end{cases}$$

## Свойства матрицы $G(t)$:
- 1) $\frac{d}{dt} G(t) = A \cdot G(t), \quad t \neq 0$
- 2) $G(+0) - G(-0) = E$
- 3) $\sup_{t \in \mathbb{R}} \| G(t) \| < \infty$

### Опр.
Матрица $G(t) \in C^1(-\infty, 0) \cap C^1(0, \infty)$ называется матрицей Грина кр. з. (2), если она удовлетворяет условиям 1-3.

### Th 2
Пусть выполнено предположение (*) $\Rightarrow \exists!$ матрица Грина краевой задачи (2), при этом решение $y(t)$ кр. з. (2) имеет вид (3).

### Доказательство
$\square$
- Из св-ва (1): $G(t) = \begin{cases} e^{tA} P, & t > 0 \\ e^{tA} Q, & t < 0 \end{cases}, \quad P, Q - n \times n$
- Из св-ва (2): $P - Q = E \Rightarrow Q = P - E$

 --- 

photo_2026-05-01 12.42.04 PM.jpeg -- 53

 --- 

# Св-во 3

### Случай 1
$\forall \lambda \in Sp(A) \quad \operatorname{Re} \lambda < 0$
$$ Q = 0, \quad P = E $$

### Случай 2
$\forall \lambda \in Sp(A) \quad \operatorname{Re} \lambda > 0$
$$ P = 0, \quad Q = -E $$

### Случай 3 (общий)
$$ A = T^{-1} \begin{pmatrix} A_- & 0 \\ 0 & A_+ \end{pmatrix} T $$
$$ e^{tA} = T^{-1} \begin{pmatrix} e^{tA_-} & 0 \\ 0 & e^{tA_+} \end{pmatrix} T $$
$$ \begin{matrix} P = T^{-1} \begin{pmatrix} E & 0 \\ 0 & 0 \end{pmatrix} T \\ Q = -T^{-1} \begin{pmatrix} 0 & 0 \\ 0 & E \end{pmatrix} T \end{matrix} \Rightarrow G(t) = \begin{cases} T^{-1} \begin{pmatrix} e^{tA_-} & 0 \\ 0 & 0 \end{pmatrix} T, & t > 0 \\ -T^{-1} \begin{pmatrix} 0 & 0 \\ 0 & e^{tA_+} \end{pmatrix} T, & t < 0 \end{cases} \blacksquare $$

Для уравнения $P_n \left( \frac{d}{dt} \right) u = h(t)$ (1.1)

Рассмотрим кр. з. (краевую задачу):
$$ \begin{cases} P_n \left( \frac{d}{dt} \right) u = h(t), t \in \mathbb{R} \\ \sup_{t \in \mathbb{R}} |u(t)| < +\infty \end{cases} \text{ (2.2)} $$

$y(t) = \begin{pmatrix} u(t) \\ \vdots \\ u^{(n-1)}(t) \end{pmatrix}; \quad (2.2) \sim \frac{dy}{dt} = A_n y + f(t); \quad A_n = \begin{pmatrix} 0 & 1 & & 0 \\ \vdots & \ddots & \ddots & \\ 0 & & & 1 \\ -a_n & & \dots & -a_1 \end{pmatrix}; \quad f(t) = \begin{pmatrix} 0 \\ \vdots \\ 0 \\ h(t) \end{pmatrix}$

$P_n \left( \frac{d}{dt} \right) = \frac{d^n}{dt^n} + a_1 \frac{d^{n-1}}{dt^{n-1}} + \dots + a_n E$

### Лемма 1
$\lambda$ является корнем уравнения $P_n(\lambda) = 0 \iff \lambda \in Sp(A_n)$ (док-во сам.)

### Th 3
Пусть $\forall \lambda: P_n(\lambda) = 0 \Rightarrow \operatorname{Re} \lambda \neq 0$ (корни хар. полинома не чисто мнимые) $\Rightarrow \forall$ ограниченной $h(t) \in C(\mathbb{R}) \exists!$ реш. $u(t)$ кр. з. (2.2), при этом:
$$ \sup_{t \in \mathbb{R}} |u(t)| \le C \cdot \sup_{t \in \mathbb{R}} |h(t)| $$

### Д:
Рассмотрим краевую задачу:
$$ \begin{cases} \frac{dy}{dt} = A_n y + f(t), t \in \mathbb{R} \\ \sup_{t \in \mathbb{R}} \|y(t)\| < +\infty \end{cases} \text{ (2.3)}, \quad f(t) = \begin{pmatrix} 0 \\ \vdots \\ h(t) \end{pmatrix} $$
$\forall \lambda: P_n(\lambda) = 0 \Rightarrow \operatorname{Re} \lambda \neq 0$. В силу леммы 1 получим, что $\forall \lambda \in Sp(A_n) \quad \operatorname{Re} \lambda \neq 0$.

 --- 

photo_2026-05-01 12.42.07 PM.jpeg -- 54

 --- 

$h(t)$ — непрерывная и ограниченная $\Rightarrow f(t) = \begin{pmatrix} 0 \\ \vdots \\ h(t) \end{pmatrix}$ — [НРЗБ: непр. и огр.]
В силу Th 1 $\exists!$ решение кр. з. (2.3) и справедлива оценка (4)
$$ \|y(t)\| \le C \cdot \sup_{s \in \mathbb{R}} \|f(s)\| \Rightarrow |u(t)| \le C \cdot \sup_{s \in \mathbb{R}} |h(s)| \sim \sup_{s \in \mathbb{R}} |u(s)| \le C \sup_{s \in \mathbb{R}} |h(s)| $$
расписывали матрицу и оценивали $\blacksquare$

### Th 4
Пусть $\forall \lambda \quad P_n(\lambda) = 0 \Rightarrow \operatorname{Re} \lambda \neq 0$ (корни хар. полинома не чисто мнимые)
$\Rightarrow \exists!$ функция $g(t) \in C^\infty(-\infty, 0) \cap C^\infty(0, \infty)$ удовлетворяющая свойствам:
- 1) $P_n(\frac{d}{dt}) g(t) = 0, t \neq 0$
- 2) $g(+0) - g(-0) = 0$
  $g'(+0) - g'(-0) = 0$
  $\dots$
  $g^{(n-2)}(+0) - g^{(n-2)}(-0) = 0$
  $g^{(n-1)}(+0) - g^{(n-1)}(-0) = 1$
- 3) $\sup_{t \in \mathbb{R}} |g(t)| < \infty$

При этом решение $u(t)$ кр. з. (2.2) имеет вид: $u(t) = \int_{-\infty}^\infty g(t-s) h(s) ds$

### Доказательство
кр. з. (2.2) $\sim \begin{cases} \frac{d}{dt} y = A_n y + \begin{pmatrix} 0 \\ \vdots \\ h(t) \end{pmatrix} \\ \sup_{t \in \mathbb{R}} \|y(t)\| < \infty \end{cases}$
$$ y(t) = \int_{-\infty}^\infty G(t-s) \begin{pmatrix} 0 \\ \vdots \\ h(s) \end{pmatrix} ds = \int_{-\infty}^\infty \begin{pmatrix} g_{11}(t-s) & \dots & g_{1n}(t-s) \\ \vdots & \ddots & \vdots \\ g_{n1}(t-s) & \dots & g_{nn}(t-s) \end{pmatrix} \begin{pmatrix} 0 \\ \vdots \\ h(s) \end{pmatrix} ds $$
$$ u(t) = \int_{-\infty}^\infty g_{1n}(t-s) h(s) ds $$
св-во ① $\Rightarrow \frac{d}{dt} \begin{pmatrix} g_{1n}(t) \\ \vdots \\ g_{nn}(t) \end{pmatrix} = A_n \begin{pmatrix} g_{1n}(t) \\ \vdots \\ g_{nn}(t) \end{pmatrix} \underset{t \neq 0}{\sim} \begin{cases} g_{2n}(t) = g_{1n}'(t) \\ g_{3n}(t) = g_{1n}''(t) = g_{2n}'(t) \\ \dots \\ g_{nn}(t) = g_{1n}^{(n-1)}(t) \end{cases}$

Смотрим на последнюю строку:
$$ \frac{d g_{nn}}{d t} = -a_n g_{1n} - \dots - a_1 g_{nn} \sim (\frac{d^n}{dt^n} + a_1 \frac{d^{n-1}}{dt^{n-1}} + \dots + a_n E) g_{1n} = 0 \sim P_n(\frac{d}{dt}) g_{1n} \underset{t \neq 0}{=} 0 $$

 --- 

photo_2026-05-01 12.42.08 PM.jpeg -- 55

 --- 

Св-во 2: $G(+0) - G(-0) \equiv E$
$$\begin{pmatrix} g_1(+0) & \dots & g_n(+0) \\ \vdots & \ddots & \vdots \\ g_1^{(n-1)}(+0) & \dots & g_n^{(n-1)}(+0) \end{pmatrix} - \begin{pmatrix} g_1(-0) & \dots & g_n(-0) \\ \vdots & \ddots & \vdots \\ g_1^{(n-1)}(-0) & \dots & g_n^{(n-1)}(-0) \end{pmatrix} = \begin{pmatrix} 0 \\ \vdots \\ 1 \end{pmatrix}$$
$2^o \uparrow$

Св-во (3) $\to$ св-во (3*) $\blacksquare$

### Опр.
Функция $g(t) \in C^n(0, \infty) \cap C^n(-\infty, 0)$, удовл. $1^o - 3^o$, называется функцией Грина.

### Как искать функцию Грина?
$1^o \Rightarrow g(t) = \begin{cases} g_1(t), & t > 0 \\ g_2(t), & t < 0 \end{cases} \quad \begin{matrix} P_n(\frac{d}{dt}) g_1(t) = 0, & t > 0 \\ P_n(\frac{d}{dt}) g_2(t) = 0, & t < 0 \end{matrix}$

$P_n(\lambda) = P_m(\lambda) \cdot P_{n-m}(\lambda)$
$\lambda_1, \dots, \lambda_m$ — корни $P_m(\lambda) : \operatorname{Re} \lambda < 0$
$\lambda_{m+1}, \dots, \lambda_n$ — корни $P_{n-m}(\lambda) : \operatorname{Re} \lambda > 0$

$M_1 = \{ \psi_1(t), \dots, \psi_m(t) \}$ — ФСР $P_m(\frac{d}{dt}) u = 0$
$M_2 = \{ \psi_{m+1}(t), \dots, \psi_n(t) \}$ — ФСР $P_{n-m}(\frac{d}{dt}) u = 0$
$\Rightarrow M = M_1 \cup M_2$ — ФСР $P_n(\frac{d}{dt}) u = 0$

$(3^*)$

# 26.02.26 лекция

## 2.5 Краевая задача на полупрямой
$$\begin{cases} \frac{dy}{dt} = Ay + f(t), & t > 0 \\ By|_{t=0} = \varphi \\ \sup_{t > 0} \|y(t)\| < +\infty \end{cases} \quad (1)$$
$A - n \times n$; $B - \mu \times n$; $\mu = 1, \dots, n$
$\varphi = \begin{pmatrix} \varphi_1 \\ \vdots \\ \varphi_\mu \end{pmatrix}$

$y(t) = y_0(t) + v(t)$
$y_0(t)$ — реш. [НРЗБ: из-за области определения]
$$\begin{cases} \frac{dy}{dt} = Ay + f(t), & t \in \mathbb{R} \\ \sup_{t \in \mathbb{R}} \|y(t)\| < +\infty \end{cases} \quad (2)$$

### Предположение (-*-)
$\forall \lambda \in \sigma(A) \quad \operatorname{Re} \lambda \neq 0$

---
*Боковая колонка (черновик/дополнения):*
$f(t) = \{ \dots$
$\frac{dy}{dt} = Ay$
$By|_{t=0} = \dots$
$\sup \|y(t)\| < \dots$
Решение [НРЗБ]
$A = T [НРЗБ] T^{-1}$
$G(t) = \begin{cases} e^{tA} \dots \\ e^{tA} \dots \end{cases}$
$\operatorname{Sp} A = \{ \dots$
$\operatorname{Sp} A_- = \{ \dots$
$\operatorname{Sp} A_+ = \{ \dots$
$T^{-1} = \{ \dots$
$P^2 = P$
$(E - P)^2 = [НРЗБ]$
$P e^{tA} = e^{tA} P$
Введем $E$ [НРЗБ]
$E^-$ — под[НРЗБ:пространство], инвариантное [НРЗБ], лежащее [НРЗБ]
$E^+$ — под[НРЗБ]
Если $x \in \dots$

 --- 

photo_2026-05-01 12.42.10 PM.jpeg -- 56

 --- 

# Краевые задачи и функции Грина

$$\overline{f}(t) = \begin{cases} f(t), & t \ge 0 \\ f(-t), & t \le 0 \end{cases}$$

$y(t) = \sigma(t) - \text{реш.}$

$$ \begin{cases} \frac{dy}{dt} = Ay, & t \ge 0 \\ By|_{t=0} = \varphi - By_0|_{t=0} = \overline{\varphi} \end{cases} \quad (3) $$

$$ \sup_{t \ge 0} \| y(t) \| < + \infty $$

Решение $y_0(t)$ краевой задачи (2) имеет вид: $$y_0(t) = \int_{-\infty}^{+\infty} G(t-s) \overline{f}(s) ds$$

$$ A = T^{-1} \begin{pmatrix} A_- & 0 \\ 0 & A_+ \end{pmatrix} T, \quad P = T^{-1} \begin{pmatrix} E & 0 \\ 0 & 0 \end{pmatrix} T, $$

$$ G(t) = \begin{cases} e^{tA} P, & t > 0 \\ e^{tA} (P - E), & t < 0 \end{cases} = \begin{cases} T^{-1} \begin{pmatrix} e^{tA_-} & 0 \\ 0 & 0 \end{pmatrix} T \\ T^{-1} \begin{pmatrix} 0 & 0 \\ 0 & -e^{tA_+} \end{pmatrix} T \end{cases} $$

- $Sp A = \{ \lambda_1, \dots, \lambda_m, \lambda_{m+1}, \dots, \lambda_n \}$
- $Sp A_- = \{ \lambda_1, \dots, \lambda_m \}, \quad \operatorname{Re} \lambda_i < 0, \quad i = 1, \dots, m$
- $Sp A_+ = \{ \lambda_{m+1}, \dots, \lambda_n \}, \quad \operatorname{Re} \lambda_j > 0, \quad j = m+1, \dots, n$
- $T^{-1} = \{ \underbrace{v_1, v_2, \dots, v_m}_{S}, \underbrace{v_{m+1}, \dots, v_n}_{S_n} \}$

- $P^2 = P$ (т.е. $P$ проектор)
- $(E - P)^2 = E - P$
- $P e^{tA} = e^{tA} P$

Введем $E^-$ и $E^+$:
- $E^-$ — подпространство, базис которого $\{ v_1, \dots, v_m \}$, т.е. $E^-$ — максимальное инвариантное подпространство, отвечающее собственным значениям матрицы $A$, лежащим в левой полуплоскости.
- $E^+$ — подпр-во, базис которого $\{ v_{m+1}, \dots, v_n \}$ — // —

### Лемма
Если $x \in E^- \Rightarrow Px = x$

### Доказательство
$$x \in E^- \Rightarrow \exists \alpha_1, \dots, \alpha_m$$
$$x = \sum_{i=1}^m \alpha_i v_i = T^{-1} \begin{pmatrix} \alpha_1 \\ \vdots \\ \alpha_m \\ 0 \\ \vdots \\ 0 \end{pmatrix}$$
$$Px = T^{-1} \begin{pmatrix} E & 0 \\ 0 & 0 \end{pmatrix} T T^{-1} \begin{pmatrix} \alpha_1 \\ \vdots \\ \alpha_m \\ 0 \\ \vdots \\ 0 \end{pmatrix} = T^{-1} \begin{pmatrix} \alpha_1 \\ \vdots \\ \alpha_m \\ 0 \\ \vdots \\ 0 \end{pmatrix} = x$$

 --- 

photo_2026-05-01 12.42.11 PM.jpeg -- 57

 --- 

### Лемма 2
Пусть выполнено предп. ($*$). Тогда след. утв. эквивалентны:
1) Реш. $y(t)$ сист $\frac{dy}{dt} = Ay$ является огр. при $t \ge 0$
2) $y(0) \in E^-$

### Доказательство
**$\Rightarrow$:** Пусть $y(t)$ — ограниченное при $t \ge 0$ решение $\frac{dy}{dt} = Ay$
$$y(t) = e^{At} y(0) = \underbrace{e^{At} P y(0)}_{y_1(t)} + \underbrace{e^{At} (E - P) y(0)}_{y_2(t)}$$
$$y_1(t) = e^{At} P y(0) = T^{-1} \begin{pmatrix} e^{A_- t} & 0 \\ 0 & e^{A_+ t} \end{pmatrix} T \cdot T^{-1} \begin{pmatrix} E & 0 \\ 0 & 0 \end{pmatrix} T y(0) = T^{-1} \begin{pmatrix} e^{A_- t} & 0 \\ 0 & 0 \end{pmatrix} T y(0)$$
В силу оценки Гельфанда-Шилова $y_1(t)$ огр. при $t \ge 0$ (более того $\|y_1(t)\| \to 0$ при $t \to \infty$)
$\Rightarrow y_2(t)$ огр. при $t \ge 0$
$$(E-P) y_2(t) = (E-P) e^{At} (E-P) y(0) = e^{At} (E-P)^2 y(0) = e^{At} (E-P) y(0) \Rightarrow$$
$$\Rightarrow \|(E-P) y(0)\| \le \|e^{-At} (E-P)\| \cdot \|y_2(t)\| \quad (*)$$
$$e^{-At} (E-P) = T^{-1} \begin{pmatrix} e^{-A_- t} & 0 \\ 0 & e^{-A_+ t} \end{pmatrix} T T^{-1} \begin{pmatrix} 0 & 0 \\ 0 & E \end{pmatrix} T = T^{-1} \begin{pmatrix} 0 & 0 \\ 0 & e^{-A_+ t} \end{pmatrix} T$$
$$Sp(-A_+) = \{-\lambda_{m+1}, \dots, -\lambda_n\}$$
$$Re(-\lambda_j) < 0, \quad j = m+1, \dots, n$$
$$\|e^{-A_+ t} (E-P)\| \to 0 \text{ при } t \to \infty \Rightarrow (*) = 0 \text{ а т.к. оценивали норму под нормой выражение } \ge 0$$
$$(E-P) y(0) = 0 \sim T^{-1} \begin{pmatrix} 0 & 0 \\ 0 & E \end{pmatrix} T y(0) = 0 \sim T y(0) = \begin{pmatrix} \alpha_1 \\ \vdots \\ \alpha_m \\ 0 \\ \vdots \\ 0 \end{pmatrix} \Rightarrow$$
$$\Rightarrow y(0) = T^{-1} \begin{pmatrix} \alpha_1 \\ \vdots \\ \alpha_m \\ 0 \\ \vdots \\ 0 \end{pmatrix} = S \begin{pmatrix} \alpha_1 \\ \vdots \\ \alpha_m \\ 0 \\ \vdots \\ 0 \end{pmatrix} = \sum_{i=1}^m \alpha_i v_i \sim y(0) \in E^-$$

**$\Leftarrow$:** Пусть $y(0) \in E^-$, т.е. $\exists \alpha_1, \dots, \alpha_m \mid y(0) = \sum_{i=1}^m \alpha_i v_i = S \begin{pmatrix} \alpha_1 \\ \vdots \\ \alpha_m \\ 0 \\ \vdots \\ 0 \end{pmatrix} = T^{-1} \begin{pmatrix} \alpha_1 \\ \vdots \\ \alpha_m \\ 0 \\ \vdots \\ 0 \end{pmatrix}$
$$y(t) = e^{At} y(0) = T^{-1} \begin{pmatrix} e^{A_- t} & 0 \\ 0 & e^{A_+ t} \end{pmatrix} T T^{-1} \begin{pmatrix} \alpha_1 \\ \vdots \\ \alpha_m \\ 0 \\ \vdots \\ 0 \end{pmatrix} =$$
$$= S e^{A_- t} \begin{pmatrix} \alpha_1 \\ \vdots \\ \alpha_m \end{pmatrix} \text{ — огр. при } t \ge 0 \text{ по Гельфанду-Шилову.}$$
Лемма доказана. $\blacksquare$

 --- 

photo_2026-05-01 12.42.55 PM.jpeg -- 58

 --- 

# Краевые задачи для систем и уравнений высших порядков

Любое огр. при $t > 0$ реш. $\frac{dy}{dt} = Ay$ имеет вид: $y(t) = S \begin{pmatrix} e^{t J_-} \\ 0 \end{pmatrix} \begin{pmatrix} c_1 \\ \vdots \\ c_m \end{pmatrix}$

[НРЗБ: н-и]:
$$B y|_{t=0} = \varphi \rightsquigarrow \underbrace{B}_{m \times n} \underbrace{S \begin{pmatrix} I \\ 0 \end{pmatrix}}_{n \times m} \begin{pmatrix} c_1 \\ \vdots \\ c_m \end{pmatrix} = \varphi$$

Условие однозначной разрешимости: $\det (B S_-) \neq 0$ — условие Лопатинского

## Тн 1 (Лопатинского)

Пусть выполнено предп. (☼) и $m \ge 1$. Тогда след. условия эквивалентны:

1) $\forall \varphi, \forall$ ограниченного и непрерывного $f(t)$ $\exists!$ решение краевой задачи (1) и при этом справедлива оценка:
$$\sup_{t \ge 0} \|y(t)\| \le C \cdot \left( \sup_{t \ge 0} \|f(t)\| + \|\varphi\| \right)$$
*(доказано ранее; соберем вместе)*

2) $\det (B S_-) \neq 0$ — условие Лопатинского.

### Следствие
Пусть выполнено предп. (☼) и $m=n \Rightarrow$ условие Лопатинского имеет след. вид: $\det B [НРЗБ]$

## Рассмотрим дифференциальное уравнение высокого порядка:
$$u^{(n)} + a_1 u^{(n-1)} + \dots + a_n u = h(t)$$
$$P_n\left(\frac{d}{dt}\right) = \frac{d^n}{dt^n} + a_1 \frac{d^{n-1}}{dt^{n-1}} + \dots + a_n E$$
$$P_n\left(\frac{d}{dt}\right) u = h(t)$$

### Предположение (🔲)
$\forall \lambda : P_n(\lambda) = 0 \Rightarrow \operatorname{Re} \lambda \neq 0$
- $\lambda_1, \dots, \lambda_m \mid \operatorname{Re} \lambda_j < 0$
- $\lambda_{m+1}, \dots, \lambda_n \mid \operatorname{Re} \lambda_j > 0$

$$P(\lambda) = \prod_{i=1}^n (\lambda - \lambda_i)$$
$$P_-(\lambda) = \prod_{j=1}^m (\lambda - \lambda_j)$$
$$P(\lambda) = \underbrace{P_-(\lambda) \cdot P_+(\lambda)}_{\text{взаимнопросты}}$$

**Введем оп. оператор:** $b_j\left(\frac{d}{dt}\right) = b_{j1} E + b_{j2} \frac{d}{dt} + \dots + b_{jn} \frac{d^{n-1}}{dt^{n-1}}$

$$\begin{cases} P_n\left(\frac{d}{dt}\right) u = h(t), \quad t > 0 \\ b_j\left(\frac{d}{dt}\right) u = \varphi_j, \quad j = 1, \dots, m \\ \sup_{t \ge 0} |u(t)| < \infty \end{cases} \quad (4)$$

 --- 

photo_2026-05-01 12.42.56 PM.jpeg -- 59

 --- 

# 05.03. 26 лекция

Введем: $b_j(\lambda) = b_{j1} + b_{j2}\lambda + \dots + b_{jn}\lambda^{n-1}$
$b_j(\lambda) = q_j(\lambda) P_-(\lambda) + \beta_j(\lambda)$
$\beta_j(\lambda) = \beta_{j1} + \beta_{j2}\lambda + \dots + \beta_{jm}\lambda^{m-1}$
$b_j(\frac{d}{dt}) = q_j(\frac{d}{dt}) P_-(\frac{d}{dt}) + \beta_j(\frac{d}{dt})$

Введем матрицу:
$$B = \begin{pmatrix} \beta_{11} & \dots & \beta_{1m} \\ \vdots & \ddots & \vdots \\ \beta_{m1} & \dots & \beta_{mm} \end{pmatrix}$$

## Th 2 (Лопатинского)

Пусть выполнено предп. ([НРЗБ]) и $m \ge 1$ и $h(t) \equiv 0$. Тогда след. утверждения эквивалентны:
- 1) $\forall \varphi_j, j=1, \dots, m \quad \exists!$ решение кр. зад. (4)
- 2) $\det B \neq 0$

### Доказательство
$\square: u(t)$ — ограниченное при $t \ge 0$ решение $P_n(\frac{d}{dt})u = 0 \iff u(t)$ — решение $P_-(\frac{d}{dt})u = 0$.
$b_j(\frac{d}{dt})u = q_j(\frac{d}{dt}) P_-(\frac{d}{dt})u + \beta_j(\frac{d}{dt})u = \beta_j(\frac{d}{dt})u$, тогда
$b_j(\frac{d}{dt})u \big|_{t=0} = \varphi_j, j=1, \dots, m \sim \begin{pmatrix} \beta_{11} & \dots & \beta_{1m} \\ \vdots & \ddots & \vdots \\ \beta_{m1} & \dots & \beta_{mm} \end{pmatrix} \begin{pmatrix} u(0) \\ \vdots \\ u^{(m-1)}(0) \end{pmatrix} = \begin{pmatrix} \varphi_1 \\ \vdots \\ \varphi_m \end{pmatrix}$.
Т.к. $u(t)$ — реш. $P_-(\frac{d}{dt})u = 0$, то $u(t)$ однозначно определяется через $u(0), u'(0), \dots, u^{(m-1)}(0) \iff \det B \neq 0$. $\blacksquare$

Если $h(t) \neq 0$:
$u(t) = u_0(t) + v(t)$
$u_0(t) = \int_{-\infty}^{+\infty} g(t-s)h(s) \, ds$ — реш. $\begin{cases} P_n(\frac{d}{dt})u = h(t), t \in \mathbb{R} \\ \sup_{t \in \mathbb{R}} \|u(t)\| < +\infty \end{cases}$
$v(t)$ — реш. $\begin{cases} P_n(\frac{d}{dt})v = 0, t \ge 0 \\ b_j(\frac{d}{dt})v \big|_{t=0} = \varphi_j - b_j(\frac{d}{dt})u_0 \big|_{t=0} \\ \sup_{t \ge 0} \|v(t)\| < +\infty \end{cases}$

 --- 

photo_2026-05-01 12.42.57 PM.jpeg -- 60

 --- 

# Th 3 (Лопатинского)

### Теорема
Пусть выполнено предп. $(\boxplus)$, $m \ge 1$. Тогда след. утв. эквивалентны:
1) $\forall \varphi_j, j = 1, \dots, m$ и ограниченной непрерывной $h(t) \exists!$ реш. кр. задачи (4)
2) $\det B \neq 0$

### Следствие
Пусть выполнено предп. $(\boxplus)$, $m \ge 1$ и $\det B \neq 0 \Rightarrow \sup_{t \ge 0} |u(t)| \le C \left( \sup_{t \ge 0} |h(t)| + \sum_{j=1}^m |\varphi_j| \right)$

## §3 Краевая задача на интервале

$$
\begin{cases} 
\frac{dy}{dt} = A(t)y + f(t), t \in (a, b) \\
Ly|_{t=a} + Ry|_{t=b} = \varphi 
\end{cases} \quad (1)
$$

$A(t) \in C([a, b]) - n \times n$; $f(t) \in C([a, b])$; $L, R - n \times n$

### Th 1
Пусть $f(t) \equiv 0$. Тогда следующие утверждения эквивалентны:
1) $\forall \varphi \exists$ реш. кр. з. (1)
2) При $\varphi = 0$ кр. з. (1) имеет только тривиальное решение (ноль)
3) $\det (L Y(a) + R Y(b)) \neq 0$; $Y(t)$ — ФМР $\frac{dy}{dt} = A(t)y$

### Доказательство (П:)
Решение $\frac{dy}{dt} = A(t)y$ имеет вид: $y(t) = Y(t) c, c = \begin{pmatrix} c_1 \\ \vdots \\ c_n \end{pmatrix}$
$(L Y(a) + R Y(b)) c = \varphi$
у.д.ё [НРЗБ]

> **Факты из алгебры**
> $B x = \psi$ СУЭ
> 1) $\forall \psi \exists$ реш. $x$
> 2) $\psi = 0 \Rightarrow$ есть ток. нулевое реш.
> 3) $\det B \neq 0$

Покажем, что пункт 3) не зависит от выбора ФМР $Y(t)$.
$Y_1(t), Y_2(t)$ — ФМР для $\frac{dy}{dt} = A(t)y$
$\Delta_1 = \det (L Y_1(a) + R Y_1(b))$
$\Delta_2 = \det (L Y_2(a) + R Y_2(b))$
$Y_1(t), Y_2(t) - ФМР \Rightarrow \exists B \mid \det B \neq 0$
$Y_2(t) = Y_1(t) \cdot B \Rightarrow \Delta_2 = \det ((L Y_1(a) + R Y_1(b)) B) = \Delta_1 \cdot \det B \neq 0$

### Следствие
Пусть $\det (L Y(a) + R Y(b)) \neq 0$ и $f(t) \equiv 0 \Rightarrow y(t) = Y(t) (L Y(a) + R Y(b))^{-1} \varphi$

 --- 

photo_2026-05-01 12.42.58 PM.jpeg -- 61

 --- 

### Th 2
Пусть $\det (L Y(a) + R Y(b)) \neq 0 \Rightarrow \forall f(t) \in C[a,b] \ \forall \varphi \ \exists!$ решение кр. задачи (1), которое имеет след. вид:
$$y(t) = Y(t) (L Y(a) + R Y(b))^{-1} (\varphi - R h) + \int_{a}^{t} Y(t) Y^{-1}(s) f(s) ds, \text{ где}$$
$$h = \int_{a}^{b} Y(b) Y^{-1}(s) f(s) ds$$

### Док:
Решение $\frac{dy}{dt} = A(t)y + f(t)$ имеет след. вид:
$$y(t) = Y(t)c + \int_{a}^{t} Y(t) Y^{-1}(s) f(s) ds$$
Подставим в краевое условие:
$$L(Y(a) \cdot c + 0) + R \left( Y(b)c + \int_{a}^{b} Y(b) Y^{-1}(s) f(s) ds \right) = \varphi$$
$$(L Y(a) + R Y(b)) c = \varphi - R h$$
$$\Rightarrow c = (L Y(a) + R Y(b))^{-1} (\varphi - R h)$$

При $\varphi = 0$:
$$y(t) = - Y(t) (L Y(a) + R Y(b))^{-1} R \int_{a}^{b} Y(b) Y^{-1}(s) f(s) ds + \int_{a}^{t} Y(t) Y^{-1}(s) f(s) ds =$$
$$= \int_{a}^{b} Y(t) [\underbrace{-(L Y(a) + R Y(b))^{-1} R Y(b)}_{W} + \theta(t-s) E] Y^{-1}(s) f(s) ds \ominus$$
$$\ominus \int_{a}^{b} Y(t) (W + \theta(t-s) E) Y^{-1}(s) f(s) ds$$

Пусть $G(t,s) = \begin{cases} Y(t) (W + E) Y^{-1}(s), & a \leq s \leq t \leq b \\ Y(t) W Y^{-1}(s), & a \leq t < s \leq b \end{cases}$
$\Rightarrow y(t) = \int_{a}^{b} G(t,s) f(s) ds$ (при $\varphi = 0$)

### Св-ва матрицы $G(t,s)$
- 1) $\frac{\partial}{\partial t} G(t,s) = A(t) G(t,s), \quad t \neq s$
- 2) $G(s+0, s) - G(s-0, s) = E$
- 3) $L G(a,s) + R G(b,s) = 0$

### Опр.
**Матрица Грина** кр. з. (1) при $\varphi = 0$ — матрица $G(t,s)$, $t \in [a,b]$, $s \in (a,b)$ удовл. св-м 1-3.

 --- 

photo_2026-05-01 12.43.00 PM.jpeg -- 62

 --- 

# Матрица Грина в краевых задачах

### Th 3
Пусть $\det(L Y(a) + R Y(b)) \neq 0 \Rightarrow$ матрица Грина опред. единственна.

 --- 

