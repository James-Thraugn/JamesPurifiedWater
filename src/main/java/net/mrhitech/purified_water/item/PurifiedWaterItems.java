package net.mrhitech.purified_water.item;

import net.dries007.tfc.util.Helpers;
import net.minecraft.world.item.BucketItem;
import net.minecraft.world.item.Item;
import net.minecraft.world.item.Items;
import net.minecraftforge.eventbus.api.IEventBus;
import net.minecraftforge.registries.DeferredRegister;
import net.minecraftforge.registries.ForgeRegistries;
import net.minecraftforge.registries.RegistryObject;
import net.mrhitech.purified_water.PurifiedWater;
import net.mrhitech.purified_water.common.Waterlikes;
import net.mrhitech.purified_water.common.fluids.PurifiedWaterFluids;

import java.util.Map;

public class PurifiedWaterItems {
    public static final DeferredRegister<Item> ITEMS = DeferredRegister.create(ForgeRegistries.ITEMS, PurifiedWater.MOD_ID);
    
    public static final Map<Waterlikes, RegistryObject<Item>> FLUID_BUCKETS = Helpers.mapOfKeys(Waterlikes.class, fluid ->
            ITEMS.register("bucket/" + fluid.getId(), () -> new BucketItem(PurifiedWaterFluids.WATERLIKES.get(fluid).source(), new Item.Properties().craftRemainder(Items.BUCKET).stacksTo(1))));
    
    
    public static void register(IEventBus bus) {
        ITEMS.register(bus);
    }

}
