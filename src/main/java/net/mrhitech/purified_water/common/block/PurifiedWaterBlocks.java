package net.mrhitech.purified_water.common.block;

import net.dries007.tfc.util.Helpers;
import net.minecraft.core.registries.Registries;
import net.minecraft.world.level.block.Block;
import net.minecraft.world.level.block.Blocks;
import net.minecraft.world.level.block.LiquidBlock;
import net.minecraft.world.level.block.state.BlockBehaviour;
import net.minecraftforge.eventbus.api.IEventBus;
import net.minecraftforge.registries.DeferredRegister;
import net.minecraftforge.registries.RegistryObject;
import net.mrhitech.purified_water.PurifiedWater;
import net.mrhitech.purified_water.common.Waterlikes;
import net.mrhitech.purified_water.common.fluids.PurifiedWaterFluids;

import java.util.Map;

public class PurifiedWaterBlocks {
    public static final DeferredRegister<Block> BLOCKS = DeferredRegister.create(Registries.BLOCK, PurifiedWater.MOD_ID);
    
    public static final Map<Waterlikes, RegistryObject<LiquidBlock>> WATERLIKES = Helpers.mapOfKeys(Waterlikes.class, fluid ->
            BLOCKS.register("fluid/" + fluid.getId(), () -> new LiquidBlock(PurifiedWaterFluids.WATERLIKES.get(fluid).source(), BlockBehaviour.Properties.copy(Blocks.WATER))));
    
    public static void register(IEventBus bus) {
        BLOCKS.register(bus);
    }
    
}
