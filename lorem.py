import random

loremText = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent in metus eget mi euismod iaculis. Nulla eget leo ac eros euismod efficitur. Maecenas dignissim placerat sem ut auctor. Praesent a ullamcorper arcu. Praesent id enim mi. In velit tellus, sodales eget nulla eget, tempor viverra dolor. Quisque vitae quam diam. Integer nec vehicula ex. Donec pellentesque a velit blandit cursus. Nullam id nibh at turpis accumsan ornare a non massa. Maecenas semper, risus ut pulvinar faucibus, diam ipsum tincidunt arcu, porttitor porttitor lacus lorem eget magna. Sed suscipit odio vel scelerisque malesuada. Vestibulum quis arcu congue, congue lectus id, hendrerit ante. Etiam viverra tellus lacinia erat pretium, nec imperdiet ex euismod. Ut et mattis lorem. Interdum et malesuada fames ac ante ipsum primis in faucibus. Etiam quis ullamcorper purus, id euismod enim. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Morbi tempor mi in nibh tempor, id hendrerit odio dignissim. Morbi a congue lorem. Phasellus a massa erat. Aliquam erat volutpat. Nam venenatis quis sem vitae vehicula. Suspendisse porta porta nisl id pulvinar. Fusce aliquet diam nunc, eget placerat lorem convallis eu. Suspendisse potenti. Ut ut orci vel mi convallis accumsan semper vel erat. Curabitur porttitor vestibulum ante nec posuere. Vivamus tincidunt eros eget mauris iaculis, eu malesuada elit ultrices. Aliquam erat volutpat. Cras scelerisque congue justo vel sollicitudin. Duis aliquam, justo eget imperdiet suscipit, turpis justo pharetra arcu, vel viverra erat sapien non nulla. Mauris finibus est nisi, in condimentum leo egestas sed. Curabitur sagittis lacus id risus hendrerit, eu auctor diam lacinia. Suspendisse condimentum turpis id orci porta, vel pretium mi condimentum. Phasellus et sollicitudin lacus. Vivamus ac leo sapien. Mauris sodales pharetra lectus, a maximus lorem sodales sed. Integer ac massa ac tortor placerat pretium vitae ullamcorper metus. Morbi pulvinar consectetur velit eu imperdiet. In hac habitasse platea dictumst. Nullam consequat nisi sit amet ultricies consectetur. Sed nec enim vitae nisi vulputate gravida. Vestibulum magna dolor, pretium non purus a, dapibus pretium metus. In hac habitasse platea dictumst. In lectus elit, hendrerit eget dui et, gravida mollis dui. Curabitur sed placerat lorem. Donec eget leo enim. Sed ornare mi felis, eget sollicitudin ipsum commodo et. Fusce augue eros, vulputate vitae commodo in, condimentum eu arcu. Fusce commodo, massa nec accumsan suscipit, risus mauris consectetur erat, eget porttitor sem dolor vel quam. Curabitur pharetra nunc eget cursus commodo. Aliquam erat volutpat. Donec et auctor dolor. Quisque non lacus dolor. Aliquam sed libero vitae ligula ullamcorper venenatis. Mauris imperdiet ipsum odio, ut facilisis leo dapibus non. Aenean tempor nisl lacus. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. In interdum in lorem quis dapibus. Donec hendrerit posuere nisl vel vulputate. Suspendisse sodales convallis turpis, eu sollicitudin orci elementum iaculis. Nam consequat viverra urna ac tristique. Aenean vehicula sapien ac lorem tempor, in efficitur orci aliquam. In bibendum est et ante mattis, id pharetra magna tempor. Pellentesque mi nulla, iaculis vel neque et, ullamcorper congue nunc. Nunc condimentum ut est sit."

loremArray = loremText.split(". ")

allUsers = User.objects.all()
for x in range(0,50):
    y = random.randint(1, 8)
    randomUser = allUsers[y]
    newPost = Post.objects.create(user=randomUser,body=loremArray[x])
    allFollowers = User.objects.filter(usersFollowed=randomUser)
    newPost.save()

allUsers = User.objects.all()
for x in range(1,8):
    for y in range(1,8):
        if x != y:
            if random.randint(0,2) != 2:
                allUsers[x].usersFollowed.add(allUsers[y])

