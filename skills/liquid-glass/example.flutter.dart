import 'dart:ui';
import 'package:flutter/material.dart';

class LiquidGlassToolbar extends StatelessWidget {
  const LiquidGlassToolbar({super.key, this.effectsEnabled = true});

  final bool effectsEnabled;

  @override
  Widget build(BuildContext context) {
    final toolbar = Container(
      padding: const EdgeInsets.symmetric(horizontal: 12, vertical: 8),
      decoration: BoxDecoration(
        color: effectsEnabled ? const Color(0x9EFFFFFF) : Theme.of(context).colorScheme.surface,
        border: Border.all(color: effectsEnabled ? const Color(0xB8FFFFFF) : Theme.of(context).colorScheme.outline),
        borderRadius: BorderRadius.circular(999),
      ),
      child: Row(
        mainAxisSize: MainAxisSize.min,
        children: [
          IconButton(tooltip: 'Search', onPressed: () {}, icon: const Icon(Icons.search)),
          IconButton(tooltip: 'Settings', onPressed: () {}, icon: const Icon(Icons.settings)),
        ],
      ),
    );

    if (!effectsEnabled) return toolbar;

    return ClipRRect(
      borderRadius: BorderRadius.circular(999),
      child: BackdropFilter(
        filter: ImageFilter.blur(sigmaX: 20, sigmaY: 20),
        child: toolbar,
      ),
    );
  }
}
