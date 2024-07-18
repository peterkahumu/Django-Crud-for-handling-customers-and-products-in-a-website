from django.core.management.base import BaseCommand
from Ecommerce.models import Product

class Command(BaseCommand):
    help = 'Load products into the database'

    def handle(self, *args, **kwargs):
        products = [
    {
        "name": "Wireless Mouse",
        "description": "A high-precision wireless mouse with ergonomic design.",
        "price": 19.99,
        "availability": True
    },
    {
        "name": "Mechanical Keyboard",
        "description": "A durable mechanical keyboard with customizable RGB lighting.",
        "price": 49.99,
        "availability": True
    },
    {
        "name": "27-inch Monitor",
        "description": "A high-resolution 27-inch monitor with vibrant colors.",
        "price": 199.99,
        "availability": True
    },
    {
        "name": "USB-C Hub",
        "description": "A versatile USB-C hub with multiple ports for all your devices.",
        "price": 29.99,
        "availability": True
    },
    {
        "name": "External Hard Drive",
        "description": "A 2TB external hard drive with fast data transfer speeds.",
        "price": 89.99,
        "availability": True
    },
    {
        "name": "Bluetooth Headphones",
        "description": "Comfortable Bluetooth headphones with noise cancellation.",
        "price": 59.99,
        "availability": True
    },
    {
        "name": "Smartwatch",
        "description": "A stylish smartwatch with fitness tracking features.",
        "price": 129.99,
        "availability": True
    },
    {
        "name": "Gaming Chair",
        "description": "An ergonomic gaming chair with adjustable height and lumbar support.",
        "price": 149.99,
        "availability": True
    },
    {
        "name": "Portable Speaker",
        "description": "A portable Bluetooth speaker with excellent sound quality.",
        "price": 39.99,
        "availability": True
    },
    {
        "name": "4K Action Camera",
        "description": "A compact 4K action camera with waterproof casing.",
        "price": 99.99,
        "availability": True
    },
    {
        "name": "Electric Toothbrush",
        "description": "An electric toothbrush with multiple brushing modes.",
        "price": 49.99,
        "availability": True
    },
    {
        "name": "Instant Pot",
        "description": "A versatile 7-in-1 instant pot for quick and easy cooking.",
        "price": 89.99,
        "availability": True
    },
    {
        "name": "Robot Vacuum",
        "description": "A smart robot vacuum with powerful suction and scheduling features.",
        "price": 229.99,
        "availability": True
    },
    {
        "name": "Electric Scooter",
        "description": "A foldable electric scooter with a long battery life.",
        "price": 399.99,
        "availability": True
    },
    {
        "name": "Air Fryer",
        "description": "A compact air fryer with adjustable temperature control.",
        "price": 59.99,
        "availability": True
    },
    {
        "name": "Smart Doorbell",
        "description": "A smart doorbell with HD video and two-way audio.",
        "price": 149.99,
        "availability": True
    },
    {
        "name": "Electric Kettle",
        "description": "A fast-boiling electric kettle with temperature control.",
        "price": 29.99,
        "availability": True
    },
    {
        "name": "Digital Photo Frame",
        "description": "A digital photo frame with a high-resolution display.",
        "price": 79.99,
        "availability": True
    },
    {
        "name": "Espresso Machine",
        "description": "A compact espresso machine with milk frother.",
        "price": 129.99,
        "availability": True
    },
    {
        "name": "Fitness Tracker",
        "description": "A sleek fitness tracker with heart rate monitoring.",
        "price": 49.99,
        "availability": True
    },
    {
        "name": "Electric Grill",
        "description": "An indoor electric grill with non-stick plates.",
        "price": 59.99,
        "availability": True
    },
    {
        "name": "LED Desk Lamp",
        "description": "A flexible LED desk lamp with adjustable brightness.",
        "price": 19.99,
        "availability": True
    },
    {
        "name": "Noise Cancelling Earbuds",
        "description": "Compact earbuds with active noise cancellation.",
        "price": 99.99,
        "availability": True
    },
    {
        "name": "Wi-Fi Range Extender",
        "description": "A device to extend your Wi-Fi coverage area.",
        "price": 39.99,
        "availability": True
    },
    {
        "name": "Smart Light Bulbs",
        "description": "Color-changing smart light bulbs with remote control.",
        "price": 49.99,
        "availability": True
    },
    {
        "name": "Electric Shaver",
        "description": "A rechargeable electric shaver with precision blades.",
        "price": 69.99,
        "availability": True
    },
    {
        "name": "Portable Power Bank",
        "description": "A high-capacity portable power bank for charging on the go.",
        "price": 29.99,
        "availability": True
    },
    {
        "name": "Cordless Drill",
        "description": "A powerful cordless drill with variable speed control.",
        "price": 59.99,
        "availability": True
    },
    {
        "name": "Electric Pressure Washer",
        "description": "A high-pressure washer for cleaning outdoor surfaces.",
        "price": 129.99,
        "availability": True
    },
    {
        "name": "Smart Thermostat",
        "description": "A smart thermostat with energy-saving features.",
        "price": 199.99,
        "availability": True
    },
    {
        "name": "VR Headset",
        "description": "An immersive VR headset with high-resolution display.",
        "price": 299.99,
        "availability": True
    },
    {
        "name": "Home Security Camera",
        "description": "A wireless security camera with night vision and motion detection.",
        "price": 79.99,
        "availability": True
    },
    {
        "name": "Digital Alarm Clock",
        "description": "A digital alarm clock with large display and USB charging ports.",
        "price": 29.99,
        "availability": True
    },
    {
        "name": "Compact Dehumidifier",
        "description": "A portable dehumidifier for small spaces.",
        "price": 49.99,
        "availability": True
    },
    {
        "name": "Smart Plug",
        "description": "A smart plug that allows you to control devices remotely.",
        "price": 24.99,
        "availability": True
    },
    {
        "name": "Portable Air Conditioner",
        "description": "A compact and portable air conditioner with remote control.",
        "price": 299.99,
        "availability": True
    },
    {
        "name": "Electric Blanket",
        "description": "A cozy electric blanket with adjustable heat settings.",
        "price": 69.99,
        "availability": True
    },
    {
        "name": "Smart Scale",
        "description": "A smart scale that tracks weight, body fat, and BMI.",
        "price": 49.99,
        "availability": True
    },
    {
        "name": "Rechargeable Flashlight",
        "description": "A bright rechargeable flashlight with multiple modes.",
        "price": 19.99,
        "availability": True
    },
    {
        "name": "Electric Coffee Grinder",
        "description": "A burr coffee grinder with multiple grind settings.",
        "price": 39.99,
        "availability": True
    },
    {
        "name": "Portable Projector",
        "description": "A compact projector with HD resolution and built-in speakers.",
        "price": 199.99,
        "availability": True
    },
    {
        "name": "Smart Door Lock",
        "description": "A keyless smart door lock with Bluetooth connectivity.",
        "price": 149.99,
        "availability": True
    },
    {
        "name": "Electric Skillet",
        "description": "A non-stick electric skillet with adjustable temperature control.",
        "price": 29.99,
        "availability": True
    },
    {
        "name": "Bluetooth Tracker",
        "description": "A small Bluetooth tracker for finding lost items.",
        "price": 19.99,
        "availability": True
    },
    {
        "name": "Electric Wine Opener",
        "description": "An automatic wine opener with rechargeable battery.",
        "price": 24.99,
        "availability": True
    },
    {
        "name": "Smart TV Stick",
        "description": "A streaming stick with access to popular streaming services.",
        "price": 49.99,
        "availability": True
    },
    {
        "name": "Electric Hair Clipper",
        "description": "A professional-grade hair clipper with multiple attachments.",
        "price": 59.99,
        "availability": True
    },
    {
        "name": "Wireless Charger",
        "description": "A fast wireless charger compatible with multiple devices.",
        "price": 29.99,
        "availability": True
    },
    {
        "name": "Smart Home Hub",
        "description": "A central hub for controlling smart home devices.",
        "price": 99.99,
        "availability": True
    },
    {
        "name": "Portable Bluetooth Keyboard",
        "description": "A foldable Bluetooth keyboard for tablets and smartphones.",
        "price": 39.99,
        "availability": True
    },
    {
        "name": "Electric Griddle",
        "description": "A large electric griddle with non-stick surface.",
        "price": 49.99,
        "availability": True
    },
    {
        "name": "Bluetooth Car Adapter",
        "description": "A Bluetooth adapter for hands-free calling and music streaming in your car.",
        "price": 24.99,
        "availability": True
    },
    {
        "name": "Home Theater System",
        "description": "A surround sound home theater system with subwoofer.",
        "price": 299.99,
        "availability": True
    },
    {
        "name": "Digital Piano",
        "description": "A full-size digital piano with weighted keys.",
        "price": 499.99,
        "availability": True
    },
    {
        "name": "Wireless Earbuds",
        "description": "Compact wireless earbuds with high-quality sound.",
        "price": 79.99,
        "availability": True
    },
    {
        "name": "Electric Toothbrush Set",
        "description": "An electric toothbrush set with multiple brush heads.",
        "price": 59.99,
        "availability": True
    },
    {
        "name": "Smart Refrigerator",
        "description": "A smart refrigerator with Wi-Fi connectivity and touch screen.",
        "price": 1199.99,
        "availability": True
    },
    {
        "name": "Portable Jump Starter",
        "description": "A compact jump starter for your car with built-in flashlight.",
        "price": 89.99,
        "availability": True
    },
    {
        "name": "Digital Voice Recorder",
        "description": "A digital voice recorder with high-quality audio recording.",
        "price": 39.99,
        "availability": True
    },
    {
        "name": "Smart Light Switch",
        "description": "A smart light switch that can be controlled remotely.",
        "price": 29.99,
        "availability": True
    },
    {
        "name": "Electric Lawn Mower",
        "description": "A cordless electric lawn mower with adjustable cutting height.",
        "price": 299.99,
        "availability": True
    },
    {
        "name": "Bluetooth Shower Speaker",
        "description": "A waterproof Bluetooth speaker for the shower.",
        "price": 19.99,
        "availability": True
    },
    {
        "name": "Smart Light Strip",
        "description": "A color-changing smart light strip with remote control.",
        "price": 39.99,
        "availability": True
    },
    {
        "name": "Wireless Gaming Mouse",
        "description": "A wireless gaming mouse with programmable buttons.",
        "price": 49.99,
        "availability": True
    },
    {
        "name": "Electric Can Opener",
        "description": "An electric can opener with automatic operation.",
        "price": 29.99,
        "availability": True
    },
    {
        "name": "Portable Air Purifier",
        "description": "A compact air purifier for small rooms.",
        "price": 99.99,
        "availability": True
    },
    {
        "name": "Bluetooth FM Transmitter",
        "description": "A Bluetooth FM transmitter for hands-free calling and music in your car.",
        "price": 24.99,
        "availability": True
    },
    {
        "name": "Electric Meat Grinder",
        "description": "A powerful electric meat grinder with multiple attachments.",
        "price": 89.99,
        "availability": True
    },
    {
        "name": "Smart Ceiling Fan",
        "description": "A ceiling fan with smart controls and LED light.",
        "price": 149.99,
        "availability": True
    },
    {
        "name": "Portable Electric Heater",
        "description": "A compact electric heater with adjustable thermostat.",
        "price": 39.99,
        "availability": True
    },
    {
        "name": "Bluetooth Beanie",
        "description": "A beanie with built-in Bluetooth headphones.",
        "price": 29.99,
        "availability": True
    },
    {
        "name": "Smart Microwave",
        "description": "A microwave with smart controls and voice commands.",
        "price": 199.99,
        "availability": True
    },
    {
        "name": "Electric Waffle Maker",
        "description": "A non-stick waffle maker with adjustable browning control.",
        "price": 29.99,
        "availability": True
    },
    {
        "name": "Wireless Charging Pad",
        "description": "A fast wireless charging pad for multiple devices.",
        "price": 39.99,
        "availability": True
    },
    {
        "name": "Smart LED Bulbs",
        "description": "Energy-efficient smart LED bulbs with voice control.",
        "price": 59.99,
        "availability": True
    },
    {
        "name": "Electric Wine Cooler",
        "description": "A wine cooler with adjustable temperature settings.",
        "price": 199.99,
        "availability": True
    },
    {
        "name": "Portable Mini Fridge",
        "description": "A compact mini fridge for cooling drinks and snacks.",
        "price": 49.99,
        "availability": True
    },
    {
        "name": "Smart Garage Door Opener",
        "description": "A smart garage door opener with Wi-Fi connectivity.",
        "price": 199.99,
        "availability": True
    },
    {
        "name": "Electric Popcorn Maker",
        "description": "A hot air popcorn maker for healthy snacks.",
        "price": 24.99,
        "availability": True
    },
    {
        "name": "Bluetooth Headband",
        "description": "A headband with built-in Bluetooth headphones for workouts.",
        "price": 19.99,
        "availability": True
    },
    {
        "name": "Smart Water Bottle",
        "description": "A smart water bottle that tracks your hydration.",
        "price": 39.99,
        "availability": True
    },
    {
        "name": "Electric Juicer",
        "description": "A powerful electric juicer for fresh juices.",
        "price": 59.99,
        "availability": True
    },
    {
        "name": "Smart Smoke Detector",
        "description": "A smart smoke detector with app notifications.",
        "price": 99.99,
        "availability": True
    },
    {
        "name": "Electric Hair Dryer",
        "description": "A professional-grade hair dryer with multiple heat settings.",
        "price": 49.99,
        "availability": True
    },
    {
        "name": "Wireless Soundbar",
        "description": "A wireless soundbar with subwoofer for home theater.",
        "price": 199.99,
        "availability": True
    },
    {
        "name": "Electric Treadmill",
        "description": "A compact treadmill with multiple workout programs.",
        "price": 399.99,
        "availability": True
    },
    {
        "name": "Smart Video Doorbell",
        "description": "A smart video doorbell with motion detection and night vision.",
        "price": 149.99,
        "availability": True
    }
]


        for product in products:
            Product.objects.create(
                name=product['name'],
                description=product['description'],
                price=product['price'],
                availability=product['availability']
            )

        self.stdout.write(self.style.SUCCESS('Successfully loaded products'))
