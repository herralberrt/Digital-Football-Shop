document.addEventListener("DOMContentLoaded", function () {
  const buttons = document.querySelectorAll(".add-to-cart-btn");

  buttons.forEach(button => {
    button.addEventListener("click", function () {
      const productName = this.getAttribute("data-product");

      fetch("/add_to_cart", {
        method: "POST",
        headers: {
          "Content-Type": "application/x-www-form-urlencoded",
        },
        body: new URLSearchParams({
          product_name: productName
        })
      })
      .then(response => response.json())
      .then(data => {
        if (data.success) {
          showNotification(`✔️ ${productName} was added to your cart!`, "success");

          // 🔄 Update the cart count live
          const cartSpan = document.querySelector(".navbar-text");
          if (cartSpan && data.cart_count !== undefined) {
            cartSpan.textContent = `Cart: ${data.cart_count}`;
          }
        } else {
          showNotification("❌ Failed to add product.", "danger");
        }
      })
      .catch(() => {
        showNotification("⚠️ Network error. Please try again.", "warning");
      });
    });
  });

  function showNotification(message, type = "success") {
    const notification = document.createElement("div");
    notification.className = `toast-message alert alert-${type}`;
    notification.textContent = message;
    document.body.appendChild(notification);

    setTimeout(() => {
      notification.remove();
    }, 2500);
  }
});
