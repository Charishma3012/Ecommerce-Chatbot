from semantic_router import Route
from semantic_router.routers import SemanticRouter
from semantic_router.encoders import HuggingFaceEncoder

encoder = HuggingFaceEncoder(
    name="sentence-transformers/all-MiniLM-L6-v2"
)

faq = Route(
    name='faq',
    utterances=[
        "What is the return policy?",
        "How do refunds work?",
        "What payment methods are accepted?",
        "Can I pay using UPI?",
        "Do you accept credit cards?",
        "What are the payment options?",
        "Can I use debit card?",
        "What is the return policy of the products?",
        "You can return products within 30 days of delivery.",
        "Do I get discount with the HDFC credit card?",
        "Yes, HDFC credit card users get a 10% discount on select items.",
        "How can I track my order?",
        "You can track your order using the tracking link sent to your email.",
        "What payment methods are accepted?",
        "We accept credit/debit cards, net banking, UPI, and cash on delivery.",
        "How long does it take to process a refund?",
        "Refunds are processed within 5-7 business days after the return is received.",
        "Are there any ongoing sales or promotions?",
        "Yes, check our 'Deals' section for ongoing sales and discounts.",
        "What is your policy on defective goods?"
    ]
)

sql = Route(
    name='sql',
    utterances=[
        "I want to buy nike shoes that have 50% discount.",
        "Are there any shoes under Rs. 3000?",
        "Do you have formal shoes in size 9?",
        "Are there any Puma shoes on sale?",
        "What is the price of puma running shoes?",
    ]
)

small_talk = Route(
    name='small_talk',
    utterances=[
        "How are you?",
        "What is your name?",
        "Tell me a joke.",
        "What's the weather like today?",
        "Do you have any hobbies?"
    ]
)

router = SemanticRouter(routes=[faq, sql, small_talk], encoder=encoder, auto_sync="local",)

if __name__ == "__main__":
    print(router("What is your policy on defective product?"))
    print(router("Pink Puma shoes in price range 5000 to 1000"))