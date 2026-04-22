import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tourism_platform.settings')
django.setup()

from places.models import Place

# NOTE: Using MongoEngine - each place is a MongoDB document
# To reset: Use MongoDB CLI -> db.places.deleteMany({})

# Add sample places with categories and cities
# INCLUDES POLLACHI AND COIMBATORE HIDDEN & LESS-EXPLORED LOCATIONS
places_data = [
    # ============================================
    # POLLACHI - HIDDEN SPOTS (New Discoveries)
    # ============================================
    {
        'name': "Loam's Viewpoint",
        'description': 'Stunning panoramic views of the Western Ghats with misty mornings. Perfect for sunrise photography and nature walks through tea plantations.',
        'location': 'Valparai Road',
        'category': 'hidden_spots',
        'city': 'pollachi'
    },
    {
        'name': 'Vazhiyar Valley',
        'description': 'A serene valley tucked away from main roads with lush green tea gardens and coffee plantations. Ideal for trekking and experiencing rural life.',
        'location': 'Valparai Area',
        'category': 'hidden_spots',
        'city': 'pollachi'
    },
    {
        'name': 'Uppar River Scenic Spot',
        'description': 'Hidden gem along Uppar River on the Anaimalai side. Crystal clear waters perfect for swimming and camping under the stars.',
        'location': 'Anaimalai Side',
        'category': 'hidden_spots',
        'city': 'pollachi'
    },
    {
        'name': 'Kaka Kothi Parai',
        'description': 'A lesser-known hilltop with 360-degree views of the surrounding valleys. Great spot for sunset watching and bird photography.',
        'location': 'Near Valparai',
        'category': 'hidden_spots',
        'city': 'pollachi'
    },
    {
        'name': 'Vettaikaranpudur Village Roads',
        'description': 'Scenic rural village routes offering authentic local experiences, traditional farming, and warm hospitality. Perfect for bike rides and village tours.',
        'location': 'Vettaikaranpudur',
        'category': 'hidden_spots',
        'city': 'pollachi'
    },
    {
        'name': 'Anikkadavu Rural Areas',
        'description': 'Unexplored rural landscape with traditional villages, rice fields, and coconut groves. Experience authentic Tamil Nadu village culture.',
        'location': 'Anikkadavu',
        'category': 'hidden_spots',
        'city': 'pollachi'
    },
    
    # ============================================
    # POLLACHI - HIDDEN WATERFALLS
    # ============================================
    {
        'name': 'Monkey Falls',
        'description': 'Cascading waterfall hidden deep in the forest, accessible through adventurous trekking. Home to playful monkeys and surrounded by dense greenery.',
        'location': 'Parambikulam Forest',
        'category': 'falls',
        'city': 'pollachi'
    },
    {
        'name': 'Panchalingam Falls',
        'description': 'Picturesque waterfall in Thirumoorthy Hills with multiple tiers and natural pools. Legend says it has five lingams formed naturally.',
        'location': 'Thirumoorthy Hills',
        'category': 'falls',
        'city': 'pollachi'
    },
    {
        'name': 'Siruvani Waterfalls',
        'description': 'Ancient waterfall known for its allegedly pure water. Surrounded by scenic hills and forests, perfect for picnics and swimming.',
        'location': 'Siruvani Mountains',
        'category': 'falls',
        'city': 'pollachi'
    },
    {
        'name': 'Aliyar Check Dam Small Waterfalls',
        'description': 'Hidden waterfall spots around Aliyar check dam. Local favorite for off-beat exploration with minimal crowds and beautiful landscape.',
        'location': 'Aliyar Dam Area',
        'category': 'falls',
        'city': 'pollachi'
    },
    
    # ============================================
    # POLLACHI - STREET FOOD AREAS
    # ============================================
    {
        'name': 'Pollachi Market Street Evening Food Zone',
        'description': 'Vibrant street food hub in the heart of Pollachi market. Authentic local snacks including murukku, laddoos, and traditional sweets.',
        'location': 'Pollachi Market',
        'category': 'food',
        'city': 'pollachi'
    },
    {
        'name': 'Mahalingapuram Night Food Streets',
        'description': 'Best-kept secret for street food lovers. Late-night food stalls serving idiyappam, paniyaram, and spicy chutneys from local recipes.',
        'location': 'Mahalingapuram',
        'category': 'food',
        'city': 'pollachi'
    },
    {
        'name': 'Fire Station Area Egg Appam Shops',
        'description': 'Famous local shops opposite the Fire Station serving fluffy egg appams and traditional breakfast items. A must-visit for morning foodies.',
        'location': 'Opposite Fire Station',
        'category': 'food',
        'city': 'pollachi'
    },
    {
        'name': 'Roadside Bajji & Bonda Shops',
        'description': 'Small, authentic roadside eateries serving crispy bajjis, bondas, and pakoras with fresh coconut chutney. Perfect for evening snacks.',
        'location': 'Various Road Junctions',
        'category': 'food',
        'city': 'pollachi'
    },
    
    # ============================================
    # POLLACHI - HIDDEN TEMPLES
    # ============================================
    {
        'name': 'Masani Amman Temple',
        'description': 'Ancient temple dedicated to Goddess Masani. Known for its spiritual significance and peaceful atmosphere away from crowded pilgrimage sites.',
        'location': 'Masani Village',
        'category': 'temple',
        'city': 'pollachi'
    },
    {
        'name': 'Bhramaram Sivan Temple',
        'description': 'Hidden Shiva temple with intricate carvings and traditional South Indian architecture. Peaceful and less crowded compared to main temples.',
        'location': 'Bhramaram',
        'category': 'temple',
        'city': 'pollachi'
    },
    {
        'name': 'Aliyar Arivu Thirukovil',
        'description': 'Serene temple located near Aliyar dam with scenic backdrops. Offers spiritual solace and stunning views of water and surrounding hills.',
        'location': 'Aliyar Area',
        'category': 'temple',
        'city': 'pollachi'
    },
    {
        'name': 'Small Village Vinayagar Temples',
        'description': 'Charming small temples dedicated to Lord Ganesha scattered across rural Pollachi villages. Each has unique local legends and architectural styles.',
        'location': 'Various Villages',
        'category': 'temple',
        'city': 'pollachi'
    },
    
    # ============================================
    # COIMBATORE - HIDDEN SPOTS
    # ============================================
    {
        'name': 'Vellingiri Hill Foothills',
        'description': 'Serene foothills offering scenic trekking paths with views of lush green landscapes. Perfect for nature lovers seeking peaceful escapes away from city hustle.',
        'location': 'Vellingiri Range',
        'category': 'hidden_spots',
        'city': 'coimbatore'
    },
    {
        'name': 'Perumal Peak',
        'description': 'Hidden mountain peak with spectacular panoramic views and adventure trekking trails. Ideal spot for sunrise viewing and nature photography.',
        'location': 'Western Ghats',
        'category': 'hidden_spots',
        'city': 'coimbatore'
    },
    {
        'name': 'Kovai Kutralam Eco Park Back Trails',
        'description': 'Off-the-beaten-path trails in the back sections of Kovai Kutralam. Rich biodiversity with fewer tourists and authentic forest experience.',
        'location': 'Coimbatore District',
        'category': 'hidden_spots',
        'city': 'coimbatore'
    },
    {
        'name': 'Siruvani Viewpoints',
        'description': 'Lesser-known viewpoints around Siruvani offering breathtaking vistas of surrounding valleys and water sources. Great for quiet meditation.',
        'location': 'Siruvani Area',
        'category': 'hidden_spots',
        'city': 'coimbatore'
    },
    {
        'name': 'Thadagam Valley Roads',
        'description': 'Scenic valley routes with traditional villages, flower farms, and vegetable gardens. Perfect for leisurely drives and experiencing local agriculture.',
        'location': 'Thadagam Valley',
        'category': 'hidden_spots',
        'city': 'coimbatore'
    },
    
    # ============================================
    # COIMBATORE - WATERFALLS
    # ============================================
    {
        'name': 'Siruvani Waterfalls (Coimbatore)',
        'description': 'Famous for its pure water and high-quality streams. Surrounded by mountains and forests with excellent bathing spots and camping opportunities.',
        'location': 'Siruvani Mountains',
        'category': 'falls',
        'city': 'coimbatore'
    },
    {
        'name': 'Kovai Kutralam Falls',
        'description': 'Picturesque waterfall in a serene forest setting with crystal clear water pools. Popular for swimming, picnicking, and adventure activities.',
        'location': 'Coimbatore District',
        'category': 'falls',
        'city': 'coimbatore'
    },
    {
        'name': 'Vaidehi Falls',
        'description': 'Hidden waterfall surrounded by dense vegetation and wildlife. Accessible through trekking paths, less crowded but equally beautiful.',
        'location': 'near Vellingiri',
        'category': 'falls',
        'city': 'coimbatore'
    },
    {
        'name': 'Siruvani Small Stream Falls',
        'description': 'Charming small waterfalls cascading through forest streams. Perfect for nature walks and experiencing the pristine beauty of mountain water sources.',
        'location': 'Siruvani Range',
        'category': 'falls',
        'city': 'coimbatore'
    },
    
    # ============================================
    # COIMBATORE - STREET FOOD AREAS
    # ============================================
    {
        'name': 'Gandhipuram Street Food Zone',
        'description': 'Vibrant wholesale market area transformed into a food paradise during evening hours. Authentic chats, samosas, and traditional South Indian snacks.',
        'location': 'Gandhipuram',
        'category': 'food',
        'city': 'coimbatore'
    },
    {
        'name': 'RS Puram Night Streets',
        'description': 'Popular nighttime food destination with numerous street vendors serving diverse cuisines. Famous for vada, idli, and spicy chaat varieties.',
        'location': 'RS Puram',
        'category': 'food',
        'city': 'coimbatore'
    },
    {
        'name': 'Town Hall Area Food Streets',
        'description': 'Historic area with traditional and modern food stalls. Home to famous local delicacies, sweets, and traditional Tamil Nadu recipes.',
        'location': 'Town Hall',
        'category': 'food',
        'city': 'coimbatore'
    },
    {
        'name': 'Brookefields Outside Street Food',
        'description': 'Emerging food street with fusion cuisine and traditional snacks. Growing destination for food enthusiasts seeking both classic and contemporary flavors.',
        'location': 'Brookefields',
        'category': 'food',
        'city': 'coimbatore'
    },
    
    # ============================================
    # COIMBATORE - TEMPLES
    # ============================================
    {
        'name': 'Eachanari Vinayagar Temple',
        'description': 'Ancient temple dedicated to Lord Ganesha with historical significance and traditional South Indian architecture. Peaceful and spiritually uplifting.',
        'location': 'Eachanari',
        'category': 'temple',
        'city': 'coimbatore'
    },
    {
        'name': 'Isha Yoga Center (Adiyogi)',
        'description': 'Modern spiritual center with the world\'s tallest Shiva statue (Adiyogi). Unique blend of ancient practices and contemporary spiritual philosophy.',
        'location': 'Vellingiri Foothills',
        'category': 'temple',
        'city': 'coimbatore'
    },
    {
        'name': 'Marudhamalai Temple',
        'description': 'Historic hilltop temple with intricate carvings and scenic surroundings. Accessible by trek or cable car with panoramic city views from the top.',
        'location': 'Marudhamalai Hills',
        'category': 'temple',
        'city': 'coimbatore'
    },
    {
        'name': 'Dhyanalinga Temple',
        'description': 'Spiritual meditation center with unique hemispherical architecture. Dedicated to inner transformation without deity worship, serene atmosphere.',
        'location': 'Velliangiri Range',
        'category': 'temple',
        'city': 'coimbatore'
    },
    
    # ============================================
    # TRICHY - HIDDEN SPOTS
    # ============================================
    {
        'name': 'Mukkombu Upper Anaicut Backwaters',
        'description': 'Scenic backwater region with peaceful boating and fishing opportunities. Surrounded by lush palm groves and traditional village settlements.',
        'location': 'Mukkombu',
        'category': 'hidden_spots',
        'city': 'trichy'
    },
    {
        'name': 'Puliyancholai Forest Route',
        'description': 'Hidden forest trail offering adventure and nature immersion. Perfect for trekking enthusiasts seeking off-the-beaten-path experiences.',
        'location': 'Puliyancholai',
        'category': 'hidden_spots',
        'city': 'trichy'
    },
    {
        'name': 'Kallanai Dam Side Trails',
        'description': 'Ancient dam with scenic walking trails and historical significance. Great spot for sunrise walks and photography of the historic structure.',
        'location': 'Kallanai',
        'category': 'hidden_spots',
        'city': 'trichy'
    },
    {
        'name': 'Uyyakondan Canal Walkways',
        'description': 'Scenic canal-side paths with agricultural vistas and rural charm. Ideal for leisurely walks through authentic Tamil Nadu countryside.',
        'location': 'Uyyakondan Canal',
        'category': 'hidden_spots',
        'city': 'trichy'
    },
    {
        'name': 'Pachamalai Hills',
        'description': 'Serene hill station with trekking trails and spiritual temples. Known for medicinal herbs and panoramic views of surrounding valleys.',
        'location': 'Pachamalai',
        'category': 'hidden_spots',
        'city': 'trichy'
    },
    
    # ============================================
    # TRICHY - WATERFALLS
    # ============================================
    {
        'name': 'Puliyancholai Waterfalls',
        'description': 'Beautiful waterfall cascading through forest terrain with natural pools. Popular trekking destination with refreshing water for swimming.',
        'location': 'Puliyancholai',
        'category': 'falls',
        'city': 'trichy'
    },
    {
        'name': 'Koraiyar Falls',
        'description': 'Hidden waterfall with scenic surroundings and lesser crowds. Accessible through forest trails with opportunities for nature photography.',
        'location': 'Koraiyar Valley',
        'category': 'falls',
        'city': 'trichy'
    },
    {
        'name': 'Pachamalai Stream Falls',
        'description': 'Small but picturesque waterfall in Pachamalai hills region. Part of scenic hill station with multiple water bodies and forest cover.',
        'location': 'Pachamalai Hills',
        'category': 'falls',
        'city': 'trichy'
    },
    
    # ============================================
    # TRICHY - STREET FOOD AREAS
    # ============================================
    {
        'name': 'Chathiram Bus Stand Street Food',
        'description': 'Bustling street food zone with authentic local cuisine and quick bites. Famous for spicy snacks and traditional Tamil Nadu breakfast items.',
        'location': 'Chathiram Bus Stand',
        'category': 'food',
        'city': 'trichy'
    },
    {
        'name': 'Thillai Nagar Food Streets',
        'description': 'Vibrant neighborhood food hub with diverse cuisine options. Popular evening hangout spot with local favorites and street vendors.',
        'location': 'Thillai Nagar',
        'category': 'food',
        'city': 'trichy'
    },
    {
        'name': 'Srirangam Temple Streets Food',
        'description': 'Temple surroundings with specialty food stalls and religious offerings. Experience authentic temple town cuisine and traditional sweets.',
        'location': 'Srirangam',
        'category': 'food',
        'city': 'trichy'
    },
    {
        'name': 'Bishop Heber College Area Food Stalls',
        'description': 'Emerging food destination popular with students and families. Mix of traditional snacks and modern fusion food options.',
        'location': 'Bishop Heber College Area',
        'category': 'food',
        'city': 'trichy'
    },
    
    # ============================================
    # TRICHY - TEMPLES
    # ============================================
    {
        'name': 'Uchi Pillayar Temple',
        'description': 'Historic hilltop temple offering panoramic city views and spiritual significance. Accessible through steps with serene surrounding atmosphere.',
        'location': 'Trichy City Center',
        'category': 'temple',
        'city': 'trichy'
    },
    {
        'name': 'Thayumanaswamy Temple',
        'description': 'Ancient Shiva temple with intricate architectural details and historical importance. Known for peaceful ambiance and devotional activities.',
        'location': 'Thiruvanaikaval',
        'category': 'temple',
        'city': 'trichy'
    },
    {
        'name': 'Jambukeswarar Temple',
        'description': 'Magnificent temple dedicated to Lord Shiva with traditional South Indian architecture. Located on an island surrounded by sacred waters.',
        'location': 'Thiruvanaikaval Island',
        'category': 'temple',
        'city': 'trichy'
    },
    {
        'name': 'Samayapuram Mariamman Temple',
        'description': 'Popular pilgrimage temple dedicated to Goddess Mariamman with grand architecture. Known for annual festivals and religious significance.',
        'location': 'Samayapuram',
        'category': 'temple',
        'city': 'trichy'
    },
    
    # ============================================
    # CHENNAI - HIDDEN SPOTS
    # ============================================
    {
        'name': 'Broken Bridge (Besant Nagar)',
        'description': 'Historic broken bridge with scenic water views and rustic charm. A hidden gem popular with photographers and locals seeking peaceful spots away from crowds.',
        'location': 'Besant Nagar',
        'category': 'hidden_spots',
        'city': 'chennai'
    },
    {
        'name': 'Theosophical Society Gardens (Adyar)',
        'description': 'Sprawling botanical gardens with spiritual heritage and diverse plant species. Serene environment perfect for meditation, walking, and connecting with nature.',
        'location': 'Adyar',
        'category': 'hidden_spots',
        'city': 'chennai'
    },
    {
        'name': 'Muttukadu Backwaters',
        'description': 'Scenic backwater ecosystem with boating opportunities and village charm. Peaceful water bodies surrounded by fishing communities and natural mangrove vegetation.',
        'location': 'Muttukadu',
        'category': 'hidden_spots',
        'city': 'chennai'
    },
    {
        'name': 'Kovalam Beach Backside Areas',
        'description': 'Quiet beach areas away from main tourist spots with authentic fishing village atmosphere. Ideal for exploring local culture and enjoying serene coastal views.',
        'location': 'Kovalam',
        'category': 'hidden_spots',
        'city': 'chennai'
    },
    {
        'name': 'Pulicat Lake (Tamil Nadu side)',
        'description': 'Largest brackish water lake in Tamil Nadu with diverse bird species and scenic landscapes. Important wetland ecosystem and birdwatching destination.',
        'location': 'Pulicat',
        'category': 'hidden_spots',
        'city': 'chennai'
    },
    
    # ============================================
    # CHENNAI - WATER SPOTS
    # ============================================
    {
        'name': 'Ennore Creek',
        'description': 'Hidden creek with water activities and peaceful surroundings for kayaking and exploration. Lesser-known water body perfect for nature enthusiasts and adventure seekers.',
        'location': 'Ennore',
        'category': 'falls',
        'city': 'chennai'
    },
    {
        'name': 'Muttukadu Boat House Quiet Zones',
        'description': 'Serene boating areas with minimal crowd and pristine natural settings. Offers opportunities for boat rides, fishing, and enjoying tranquil water experiences.',
        'location': 'Muttukadu',
        'category': 'falls',
        'city': 'chennai'
    },
    {
        'name': 'Pulicat Lagoon Hidden Points',
        'description': 'Unexplored corners of Pulicat Lagoon offering solitude and natural beauty. Perfect for photography, observation, and experiencing pristine wetland ecosystems.',
        'location': 'Pulicat',
        'category': 'falls',
        'city': 'chennai'
    },
    
    # ============================================
    # CHENNAI - STREET FOOD AREAS
    # ============================================
    {
        'name': 'Sowcarpet Street Food',
        'description': 'Bustling shopping area with diverse street food vendors and local delicacies. Historic marketplace with authentic Chennai cuisine and traditional snacks.',
        'location': 'Sowcarpet',
        'category': 'food',
        'city': 'chennai'
    },
    {
        'name': 'Besant Nagar Beach Food Street',
        'description': 'Vibrant beachside food street with seafood specialties and casual dining. Popular evening spot for locals enjoying fresh catches and coastal ambiance.',
        'location': 'Besant Nagar',
        'category': 'food',
        'city': 'chennai'
    },
    {
        'name': 'T Nagar Night Food Streets',
        'description': 'Lively neighborhood food hub with evening street vendors and local favorites. Mix of traditional snacks, dosas, and modern food options for night owls.',
        'location': 'T Nagar',
        'category': 'food',
        'city': 'chennai'
    },
    {
        'name': 'Anna Nagar Food Streets',
        'description': 'Family-friendly food destination with diverse cuisine options and casual atmosphere. Popular spot for sampling authentic Chennai street food and treats.',
        'location': 'Anna Nagar',
        'category': 'food',
        'city': 'chennai'
    },
    
    # ============================================
    # CHENNAI - TEMPLES
    # ============================================
    {
        'name': 'Ashtalakshmi Temple',
        'description': 'Unique eight-armed Ashtalakshmi statue in coastal shrine with spiritual significance. Stunning architecture and peaceful waterfront location offering serene devotional experience.',
        'location': 'Besant Nagar Foreshore',
        'category': 'temple',
        'city': 'chennai'
    },
    {
        'name': 'Marundeeswarar Temple',
        'description': 'Ancient Shiva temple with historical importance and intricate carvings. Known for its therapeutic sand and devotional atmosphere in coastal setting.',
        'location': 'Muttukadu',
        'category': 'temple',
        'city': 'chennai'
    },
    {
        'name': 'Kapaleeshwarar Temple Streets',
        'description': 'Historic temple with architectural grandeur and vibrant surroundings. Located in bustling area with temple streets, shops, and traditional Tamil heritage.',
        'location': 'Mylapore',
        'category': 'temple',
        'city': 'chennai'
    },
    {
        'name': 'Iskcon Temple Chennai',
        'description': 'Modern spiritual center with Krishna consciousness teachings and vegetarian cuisine. Serene campus offering meditation, cultural programs, and peaceful ambiance.',
        'location': 'Kanakpura Road',
        'category': 'temple',
        'city': 'chennai'
    },
    
    # ============================================
    # MADURAI - HIDDEN SPOTS
    # ============================================
    {
        'name': 'Samanar Hills',
        'description': 'Scenic hill region with trekking trails and historical cave temples. Offering panoramic views of Madurai and peaceful natural surroundings with spiritual significance.',
        'location': 'Samanar Hills',
        'category': 'hidden_spots',
        'city': 'madurai'
    },
    {
        'name': 'Yanaimalai (Elephant Hill)',
        'description': 'Historic hilltop location with scenic vistas and ancient ruins. Named for elephant sightings, offers adventure trekking and nature exploration opportunities.',
        'location': 'Yanaimalai',
        'category': 'hidden_spots',
        'city': 'madurai'
    },
    {
        'name': 'Arittapatti Village',
        'description': 'Quaint rural village with authentic Tamil culture and mountain backdrop. Hidden gem for experiencing traditional lifestyle and scenic agricultural landscapes.',
        'location': 'Arittapatti',
        'category': 'hidden_spots',
        'city': 'madurai'
    },
    {
        'name': 'Vandiyur Teppakulam Backside Area',
        'description': 'Serene lake surroundings with quiet pathways and bird watching opportunities. Beautiful waterside locations away from main tourist areas.',
        'location': 'Vandiyur',
        'category': 'hidden_spots',
        'city': 'madurai'
    },
    {
        'name': 'Nagamalai Hills',
        'description': 'Scenic hills with temple ruins and natural trails for exploration. Peaceful destination for trekking, photography, and spiritual experiences.',
        'location': 'Nagamalai',
        'category': 'hidden_spots',
        'city': 'madurai'
    },
    
    # ============================================
    # MADURAI - WATER SPOTS
    # ============================================
    {
        'name': 'Sothuparai Dam',
        'description': 'Beautiful dam with scenic water views and picnic areas. Ideal destination for photography, boating, and enjoying water-based activities with natural beauty.',
        'location': 'Sothuparai',
        'category': 'falls',
        'city': 'madurai'
    },
    {
        'name': 'Vaigai River Riverside Spots',
        'description': 'Tranquil riverside areas perfect for leisurely walks and nature observation. Peaceful stretches offering local charm and scenic water vistas.',
        'location': 'Vaigai River',
        'category': 'falls',
        'city': 'madurai'
    },
    {
        'name': 'Arittapatti Water Areas',
        'description': 'Natural water sources and scenic water bodies in Arittapatti region. Great for swimming, photography, and experiencing pristine natural water ecosystems.',
        'location': 'Arittapatti',
        'category': 'falls',
        'city': 'madurai'
    },
    
    # ============================================
    # MADURAI - STREET FOOD AREAS
    # ============================================
    {
        'name': 'Madurai Night Food Street (Near Periyar Bus Stand)',
        'description': 'Popular evening food destination with diverse street vendors. Famous for authentic local cuisine, snacks, and bustling food culture atmosphere.',
        'location': 'Periyar Bus Stand Area',
        'category': 'food',
        'city': 'madurai'
    },
    {
        'name': 'Town Hall Road Food Stalls',
        'description': 'Established food hub with variety of traditional and modern options. Busy area with authentic Madurai specialties and casual dining for the masses.',
        'location': 'Town Hall Road',
        'category': 'food',
        'city': 'madurai'
    },
    {
        'name': 'Vilakkuthoon Street Food Area',
        'description': 'Vibrant neighborhood food street with mixed cuisine vendors. Popular spot for locals and visitors seeking authentic food experiences.',
        'location': 'Vilakkuthoon',
        'category': 'food',
        'city': 'madurai'
    },
    {
        'name': 'KK Nagar Street Food Spots',
        'description': 'Emerging food zone with modern and traditional food options. Family-friendly area with diverse vendors catering to various tastes.',
        'location': 'KK Nagar',
        'category': 'food',
        'city': 'madurai'
    },
    
    # ============================================
    # MADURAI - TEMPLES
    # ============================================
    {
        'name': 'Meenakshi Amman Temple Streets',
        'description': 'Iconic temple surroundings with vibrant streets and religious significance. Historic temple with architectural grandeur and bustling temple town atmosphere.',
        'location': 'Meenakshi Temple Complex',
        'category': 'temple',
        'city': 'madurai'
    },
    {
        'name': 'Koodal Azhagar Temple',
        'description': 'Ancient Vishnu temple with historical importance and serene surroundings. Peaceful devotional atmosphere with traditional South Indian architecture.',
        'location': 'Koodal Azhagar',
        'category': 'temple',
        'city': 'madurai'
    },
    {
        'name': 'Alagar Kovil',
        'description': 'Scenic hilltop temple with panoramic views of Madurai city. Spiritual destination with picturesque location and natural surroundings.',
        'location': 'Alagar Hill',
        'category': 'temple',
        'city': 'madurai'
    },
    {
        'name': 'Pazhamudhircholai Murugan Temple',
        'description': 'Hilltop Murugan temple with intricate carvings and spiritual significance. Known for pilgrimages and ancient religious architecture with scenic views.',
        'location': 'Pazhamudhircholai',
        'category': 'temple',
        'city': 'madurai'
    },

]

for place_data in places_data:
    # Check if place already exists to avoid duplicates
    existing = Place.objects(name=place_data['name'], city=place_data['city']).first()
    if not existing:
        place = Place(**place_data)
        place.save()
        print(f"[OK] Created: {place_data['name']} ({place_data['category']}) - {place_data['city']}")
    else:
        print(f"[SKIP] Already exists: {place_data['name']} - {place_data['city']}")

print(f"\nTotal places in MongoDB: {Place.objects.count()}")


