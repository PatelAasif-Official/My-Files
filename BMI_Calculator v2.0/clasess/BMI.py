class BmiCalci:
	def __init__(self,ft,inch,weight):
		self.ft = ft
		self.inch = inch
		self.weight = weight

	def bmi(self):

		meter = (self.ft/3.28)+(self.inch/39.37)
		bmi = self.weight/meter**2
		return bmi

class Tips:

	def weight_loss(self):
		
		return ("\n\n  1) Chew Thoroughly and Slow Down.\n\n  2) Use Smaller Plates for Unhealthy Foods\n\n  3) Eat Plenty of Protein.\n\n  4) Store Unhealthy Foods out of Sight.\n\n  5) Eat Fiber-Rich Foods.\n\n  6) Drink Water More Often\n\n  7) Serve Yourself Smaller Portions\n\n  8) Eat Without Electronic Distractions.\n\n  9) Sleep Well and Avoid Stress.\n\n  10 Eliminate Sugary Drinks.\n\n  11) Serve Unhealthy Food on Red Plates.\n\n  12) Do Exercise")

	def weight_gain(self):

		return ("\n\n  1) Don’t drink water before meals. This can fill your stomach and make it\n  harder to get in enough calories.\n\n  2) Eat more often. Squeeze in an additional meal or snack whenever you can,\n  such as before bed.\n\n  3) Drink milk. Drinking whole milk to quench thirst is a simple way to get\n  in more high-quality protein and calories.\n\n  4) Try weight gainer shakes. If you’re really struggling then you can try\n  weight gainer shakes. These are very high in protein, carbs and calories.\n\n  5) Use bigger plates. Definitely use large plates if you’re trying to get\n  in more calories, as smaller plates cause people to automatically eat less.\n\n  6) Add cream to your coffee. This is a simple way to add in more calories.\n\n  7) Take creatine. The muscle building supplement creatine monohydrate\n  can help you gain a few pounds in muscle weight.\n\n  8) Get quality sleep. Sleeping properly is very important for muscle growth.\n\n  9)Eat your protein first and vegetables last. If you have a mix of foods\n  on your plate, eat the calorie-dense and protein-rich foods first. Eat the\n  vegetables last.\n\n  10) Don’t smoke. Smokers tend to weigh less than non-smokers, and quitting\n  smoking often leads to weight gain.")

	def stay_healthy(self):
		
		return ("\n\n  1) Be physically active for 30 minutes most days of the week. Break this up into three 10-minute sessions when pressed for time. Healthy movement may include walking, sports, dancing, yoga, running or other activities you enjoy.\n\n  2) Eat a well-balanced, low-fat diet with lots of fruits, vegetables and whole grains. Choose a diet that's low in saturated fat and cholesterol, and moderate in sugar, salt and total fat.\n\n  3) Brush your teeth after meals with a soft or medium bristled toothbrush. Also brush after drinking and before going to bed. Use dental floss daily.\n\n  4) Stay in touch with family and friends.\n\n  5) Good ways to deal with stress include regular exercise, healthy eating habits and relaxation exercises, such as deep breathing or meditation. Talking to trusted family members and friends can help a lot. Some women find that interacting with their faith community is helpful in times of stress.\n\n  6) Don't smoke, or quit if you do. Ask your health care provider for help. UCSF's Tobacco Education Center offers smoking cessation and relapse prevention classes as well as doctor consultations for smokers trying to quit.")
	
